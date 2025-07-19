#!/bin/zsh

# List of DBC filenames
files=(
  "InterfaceBTMS_V2025-2"
  "InterfaceBattery_V2025-11"
  "InterfaceCluster_V2025-1"
  "InterfaceComponentCooling_V2025-3"
  "InterfaceControlSystem_V2025-3"
  "InterfaceDCDC_V2025-3"
  "InterfaceEVCC_V2025-4"
  "InterfaceFNV_V2025-1"
  "InterfaceHMI_V2025-15"
  "InterfaceHVAC_V2025-5"
  "InterfaceIO_V2025-6"
  "InterfaceOBC_V2025-1"
  "InterfacePowerSteering_V2025-2"
  "InterfacePowertrain_V2025-8"
  "InterfaceTelematics_V2025-3"
  "InterfaceVehicle_V2025-8"
)

# Generate empty .txt files
for name in "${files[@]}"; do
  touch "CAN/Interface/${name}.txt"
  echo "Created ${name}.txt"
done

