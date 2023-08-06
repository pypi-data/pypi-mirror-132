#!/usr/bin/python3
# -*- coding: utf8 -*-

# Copyright (c) 2021 Baidu, Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Default SchedulerPipeline for QuanlseSchedulerSuperconduct.
"""

from numpy import array

from Quanlse.Scheduler.SchedulerPipeline import SchedulerProcess, toLayer, fillUp, \
    leftAlignSingleGates, delayFirstGate, findMaxT, addToJob
from Quanlse.Scheduler import Scheduler


def _gatesBeforeMulti(layer, scheduler):
    """
    Find gate number before the first multi-qubit gate
    """
    flag = [True] * scheduler.subSysNum
    gateNumber = [len(layer)] * scheduler.subSysNum
    for i in range(len(layer[0])):
        for j in range(len(layer)):
            if layer[j][i] is not None:
                if len(layer[j][i].qubits) >= 2 and flag[i] is True:
                    gateNumber[i] = j
                    flag[i] = False
    return gateNumber


def _centerAlignedCore(scheduler: Scheduler) -> None:
    """
    The center alignment strategy for scheduling.

    :param scheduler: Scheduler object containing the circuit information
    :return: the returned QJob object
    """

    # Initialize layers
    layer = []
    for _ in range(scheduler.subSysNum):
        layer.append([])

    # First convert gates in Scheduler to layers
    toLayer(layer, scheduler, reversedOrder=True)
    fillUp(layer, qubits=None, reversedOrder=True)

    # left aligned the single-qubit gates
    leftAlignSingleGates(layer)

    # Transpose layers
    layer = array(layer).T.tolist()

    # find gate number before the first multi-qubit gates
    gatesBeforeMultiQubitGate = _gatesBeforeMulti(layer, scheduler)

    # start the first gate as late as possible
    delayFirstGate(layer, gatesBeforeMultiQubitGate)

    # find max time for each layer
    maxi = findMaxT(layer)

    # add waves to job
    addToJob(layer=layer, scheduler=scheduler, maxT=maxi)


centerAligned = SchedulerProcess("CenterAligned", _centerAlignedCore)
"""
A SchedulerProcess instance containing the center-aligned scheduling strategy.
"""
