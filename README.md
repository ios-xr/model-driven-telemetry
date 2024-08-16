## IOS XR Telemetry
This Repository contains Telemetry Protos for Cisco IOS XR yang models. It is currently organized by OS release version under protos directory.

Prior to XR software version 7.11.2, release versions are represented without the dots. Starting software version 7.11.2, the naming convention
of the folder has been changed to represent the dots with '_'. For example: protos for software version 7.11.2 are located under 'protos/7_11_2'.

For 6.2, 6.3, 6.4, 6.5, 6.6 and 7.0, maintenance versions will use 'x' instead of number in directory naming, if same protos can be used
across the maintenance releases.

Protos are organized in directory structure which matches yang model. Instructions on how to unmarshal compact gpb message can be read at
https://github.com/cisco/bigmuddy-network-telemetry-proto

Proto directory contents include,
* cisco_ios_xr_.*oper, root of native Cisco IOS XR models
* .*_yang2proto_map.json, a mapping of YANG encoding path to message set definition models. These mappings can be used to figure our gather points in models and to get message definitions to decode GPB messages.
* telemetry.proto, top level messages used with streaming telemetry and including the unified header used with GPB and GPB K/V encoding
* mdt_grpc_dialin/out, gRPC service specification for streaming telemetry server and client side streaming

GRPC services are defined in mdt_grpc_dialin/mdt_grpc_dialin.proto and mdt_grpc_dialout/mdt_grpc_dialout.proto depending on if dialin or dialout is used to stream the data. These protos will be kept backward compatible across releases.
For decoding self-describing-gpb(gpb k/v) telemetry message only telemetry.proto is required.

For more info on Model Driven Telemetry,
* https://xrdocs.io/telemetry/
* https://www.cisco.com/c/en/us/td/docs/iosxr/ncs5500/telemetry/b-telemetry-cg-ncs5500-62x/b-telemetry-cg-ncs5500-62x_chapter_010.html
 
For more info on the IOS XR Telemetry collector:
* https://github.com/ios-xr/telemetry-go-collector 
