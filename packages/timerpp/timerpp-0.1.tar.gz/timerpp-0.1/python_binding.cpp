//
// Created by nbdy on 22.12.21.
//

#include "timerpp.h"
#include <pybind11/pybind11.h>

PYBIND11_MODULE(timerpp, m) {
  pybind11::class_<timerpp::Timer> timer(m, "Timer");
  // Constructor
  timer.def(pybind11::init<timerpp::FunctionType>());
  timer.def(pybind11::init<timerpp::FunctionType, uint32_t>());
  timer.def("start", static_cast<timerpp::Timer::StartResult (timerpp::Timer::*)(void)>(&timerpp::Timer::start), "Start the timer");
  timer.def("start", static_cast<timerpp::Timer::StartResult (timerpp::Timer::*)(uint32_t)>(&timerpp::Timer::start), "Start the timer");
  timer.def("stop", static_cast<timerpp::Timer::StopResult (timerpp::Timer::*)(void)>(&timerpp::Timer::stop), "Stop the timer");
  timer.def("kill", &timerpp::Timer::kill, "Kill the timer");
  timer.def("join", &timerpp::Timer::join, "Join the timer thread");
  timer.def("is_running", &timerpp::Timer::isRunning);
  timer.def("is_armed", &timerpp::Timer::isArmed);
  timer.def("is_function_too_expensive", &timerpp::Timer::isFunctionTooExpensive);

  // Types
  // - StartResult
  pybind11::enum_<timerpp::Timer::StartResult> startResult(timer, "StartResult");
  startResult.value("START_OK", timerpp::Timer::StartResult::START_OK);
  startResult.value("ALREADY_RUNNING", timerpp::Timer::StartResult::ALREADY_RUNNING);
  startResult.value("INTERVAL_NULL", timerpp::Timer::StartResult::INTERVAL_NULL);
  startResult.value("FUNCTION_NULL", timerpp::Timer::StartResult::FUNCTION_NULL);
  // - StopResult
  pybind11::enum_<timerpp::Timer::StopResult> stopResult(timer, "StopResult");
  stopResult.value("STOP_OK", timerpp::Timer::StopResult::STOP_OK);
  stopResult.value("ALREADY_STOPPED", timerpp::Timer::StopResult::ALREADY_STOPPED);
  // Functions
}
