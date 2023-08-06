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
Quanlse Scheduler for Ion Trap quantum computing platform
"""

from Quanlse.Scheduler import Scheduler
from Quanlse.Scheduler.SchedulerPulseGenerator import SchedulerPulseGenerator
from Quanlse.TrappedIon.SchedulerSupport.DefaultPulseGenerator import defaultPulseGenerator


class SchedulerIon(Scheduler):
    """
    Basic class of Quanlse Scheduler for trapped ion platform

    :param dt: AWG sampling time
    :param generator: the pulseGenerator object.
    :param subSysNum: size of the subsystem
    :param sysLevel: the energy levels of the system (support different levels for different qubits)
    """
    def __init__(self, dt: float = None, generator: SchedulerPulseGenerator = None,
                 subSysNum: int = None, sysLevel: int = None):
        """
        Constructor for class SchedulerIon
        """

        # Initialization
        super().__init__(dt=dt, generator=generator, subSysNum=subSysNum, sysLevel=sysLevel)

        if self._pulseGenerator is None:
            self._pulseGenerator = defaultPulseGenerator()

    def plotIon(self) -> None:
        """
        Plot the ion pulses.

        :return: None
        """
        if self._ham is not None:
            self._ham.job.plotIon()
        elif self._job is not None:
            self._job.plotIon()