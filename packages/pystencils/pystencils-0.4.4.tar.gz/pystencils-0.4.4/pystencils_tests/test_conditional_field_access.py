# -*- coding: utf-8 -*-
#
# Copyright © 2019 Stephan Seitz <stephan.seitz@fau.de>
#
# Distributed under terms of the GPLv3 license.

"""

"""
import itertools

import numpy as np
import pytest
import sympy as sp

import pystencils as ps
from pystencils import Field, x_vector
from pystencils.astnodes import ConditionalFieldAccess
from pystencils.simp import sympy_cse


def add_fixed_constant_boundary_handling(assignments, with_cse):

    common_shape = next(iter(set().union(itertools.chain.from_iterable(
        [a.atoms(Field.Access) for a in assignments]
    )))).field.spatial_shape
    ndim = len(common_shape)

    def is_out_of_bound(access, shape):
        return sp.Or(*[sp.Or(a < 0, a >= s) for a, s in zip(access, shape)])

    safe_assignments = [ps.Assignment(
        assignment.lhs, assignment.rhs.subs({
            a: ConditionalFieldAccess(a, is_out_of_bound(sp.Matrix(a.offsets) + x_vector(ndim), common_shape))
            for a in assignment.rhs.atoms(Field.Access) if not a.is_absolute_access
        })) for assignment in assignments.all_assignments]

    subs = [{a: ConditionalFieldAccess(a, is_out_of_bound(
        sp.Matrix(a.offsets) + x_vector(ndim), common_shape))
        for a in assignment.rhs.atoms(Field.Access) if not a.is_absolute_access
    } for assignment in assignments.all_assignments]
    print(subs)

    if with_cse:
        safe_assignments = sympy_cse(ps.AssignmentCollection(safe_assignments))
        return safe_assignments
    else:
        return ps.AssignmentCollection(safe_assignments)


@pytest.mark.parametrize('with_cse', (False, 'with_cse'))
def test_boundary_check(with_cse):

    f, g = ps.fields("f, g : [2D]")
    stencil = ps.Assignment(g[0, 0],
                            (f[1, 0] + f[-1, 0] + f[0, 1] + f[0, -1]) / 4)

    f_arr = np.random.rand(1000, 1000)
    g_arr = np.zeros_like(f_arr)
    # kernel(f=f_arr, g=g_arr)

    assignments = add_fixed_constant_boundary_handling(ps.AssignmentCollection([stencil]), with_cse)

    print(assignments)
    kernel_checked = ps.create_kernel(assignments, ghost_layers=0).compile()
    ps.show_code(kernel_checked)

    # No SEGFAULT, please!!
    kernel_checked(f=f_arr, g=g_arr)
