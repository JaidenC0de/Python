#$localsystem = "DC-07"
#Invoke-command -ComputerName $localsystem -scriptblock
#PSSession
# Try to figure out what the process of making an inventory is
# Figure out what format i'm going to make my command in
# Get the local systems information listed before getting domains systems listed for an understanding.
Get-CimInstance -ClassName CIM_BIOSElement
Get-CimInstance -ClassName CIM_DirectoryAction
Get-CimInstance -ClassName CIM_DesktopMonitor
Get-CimInstance -ClassName CIM_Keyboard
Get-CimInstance -ClassName CIM_Memory
Get-CimInstance -ClassName CIM_OperatingSystem
