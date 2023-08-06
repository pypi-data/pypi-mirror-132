#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# from datetime import datetime
#
# from grutils import utils
# from grutils import error
# from grutils.utils import date_of

# err = error.Error()
# print(utils.int_value_of("101.12", err, 0))
#
# print(date_of(datetime.date(datetime.now())))

from grutils.progress import shared_progress

shared_progress.reset()

shared_progress.register_step("step 1", 6)
shared_progress.register_step("step 2", 4)
shared_progress.register_step("step 2.1", 0.6, ["step 2"])
shared_progress.register_step("step 2.2", 0.4, ["step 2"])
shared_progress.register_step("step 2.2.1", 1, ["step 2", "step 2.2"])
shared_progress.register_step("step 2.2.2", 1, ["step 2", "step 2.2"])
shared_progress.register_step("step 2.2.3", 1, ["step 2", "step 2.2"])
shared_progress.register_step("step 2.2.4", 1, ["step 2", "step 2.2"])
shared_progress.register_step("step 2.3", 1, ["step 2"])
shared_progress.register_step("step 3", 10)

shared_progress.re_assign_steps()

shared_progress.finish_step(["step 3"])
shared_progress.dump_steps()

shared_progress.reset()
shared_progress.finish_step(["step 2"])
shared_progress.dump_steps()


shared_progress.reset(True)
shared_progress.finish()
shared_progress.dump_steps()

# print('\n\n  ============== ')
# shared_progress.finish_step(["step 1"])
#
# print('\n\n  ============== ')
# shared_progress.finish_step(["step 2", "step 2.1"])
#
# print('\n\n  ============== ')
# shared_progress.finish_step(["step 2", "step 2.2", "step 2.2.1"])
# shared_progress.finish_step(["step 2", "step 2.2", "step 2.2.2"])
# shared_progress.finish_step(["step 2", "step 2.2", "step 2.2.3"])
# shared_progress.finish_step(["step 2", "step 2.2"])
#
# print('\n\n  ============== ')
# shared_progress.finish_step(["step 3"])
#
# print('\n\n  ============== ')
# shared_progress.finish()
# shared_progress.dump_steps()
#
# print('\n\n  ============== ')
# shared_progress.reset()
# shared_progress.dump_steps()
