
"use strict";

let CompanionProcessStatus = require('./CompanionProcessStatus.js');
let BatteryStatus = require('./BatteryStatus.js');
let AttitudeTarget = require('./AttitudeTarget.js');
let CommandCode = require('./CommandCode.js');
let RCIn = require('./RCIn.js');
let Waypoint = require('./Waypoint.js');
let HilActuatorControls = require('./HilActuatorControls.js');
let ExtendedState = require('./ExtendedState.js');
let HilSensor = require('./HilSensor.js');
let WheelOdomStamped = require('./WheelOdomStamped.js');
let RadioStatus = require('./RadioStatus.js');
let Trajectory = require('./Trajectory.js');
let HomePosition = require('./HomePosition.js');
let DebugValue = require('./DebugValue.js');
let VFR_HUD = require('./VFR_HUD.js');
let CamIMUStamp = require('./CamIMUStamp.js');
let ActuatorControl = require('./ActuatorControl.js');
let Altitude = require('./Altitude.js');
let State = require('./State.js');
let Vibration = require('./Vibration.js');
let ParamValue = require('./ParamValue.js');
let ADSBVehicle = require('./ADSBVehicle.js');
let PositionTarget = require('./PositionTarget.js');
let LogEntry = require('./LogEntry.js');
let RCOut = require('./RCOut.js');
let WaypointList = require('./WaypointList.js');
let HilControls = require('./HilControls.js');
let OverrideRCIn = require('./OverrideRCIn.js');
let GlobalPositionTarget = require('./GlobalPositionTarget.js');
let WaypointReached = require('./WaypointReached.js');
let FileEntry = require('./FileEntry.js');
let Thrust = require('./Thrust.js');
let Param = require('./Param.js');
let ManualControl = require('./ManualControl.js');
let OpticalFlowRad = require('./OpticalFlowRad.js');
let LogData = require('./LogData.js');
let HilGPS = require('./HilGPS.js');
let TimesyncStatus = require('./TimesyncStatus.js');
let StatusText = require('./StatusText.js');
let VehicleInfo = require('./VehicleInfo.js');
let Mavlink = require('./Mavlink.js');
let HilStateQuaternion = require('./HilStateQuaternion.js');
let RTCM = require('./RTCM.js');

module.exports = {
  CompanionProcessStatus: CompanionProcessStatus,
  BatteryStatus: BatteryStatus,
  AttitudeTarget: AttitudeTarget,
  CommandCode: CommandCode,
  RCIn: RCIn,
  Waypoint: Waypoint,
  HilActuatorControls: HilActuatorControls,
  ExtendedState: ExtendedState,
  HilSensor: HilSensor,
  WheelOdomStamped: WheelOdomStamped,
  RadioStatus: RadioStatus,
  Trajectory: Trajectory,
  HomePosition: HomePosition,
  DebugValue: DebugValue,
  VFR_HUD: VFR_HUD,
  CamIMUStamp: CamIMUStamp,
  ActuatorControl: ActuatorControl,
  Altitude: Altitude,
  State: State,
  Vibration: Vibration,
  ParamValue: ParamValue,
  ADSBVehicle: ADSBVehicle,
  PositionTarget: PositionTarget,
  LogEntry: LogEntry,
  RCOut: RCOut,
  WaypointList: WaypointList,
  HilControls: HilControls,
  OverrideRCIn: OverrideRCIn,
  GlobalPositionTarget: GlobalPositionTarget,
  WaypointReached: WaypointReached,
  FileEntry: FileEntry,
  Thrust: Thrust,
  Param: Param,
  ManualControl: ManualControl,
  OpticalFlowRad: OpticalFlowRad,
  LogData: LogData,
  HilGPS: HilGPS,
  TimesyncStatus: TimesyncStatus,
  StatusText: StatusText,
  VehicleInfo: VehicleInfo,
  Mavlink: Mavlink,
  HilStateQuaternion: HilStateQuaternion,
  RTCM: RTCM,
};
