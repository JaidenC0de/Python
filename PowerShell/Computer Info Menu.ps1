#Network adapter, porcessor, disk storage, memory, keyboard, and general operating system information.
Write-Host "------------Menu------------" -foreground blue
Write-Host '1 - Operating system info'
Write-Host '2 - Processor'
Write-Host '3 - Memory'
Write-Host '4 - Disk-Space'
Write-Host '5 - Keyboard'
$Select = Read-Host "select any of the following"
switch ($select) {

    '1' { Get-CimInstance -classname CIM_OperatingSystem format-} 
    '2' { Get-CimInstance -classname CIM_Processor } 
    '3' { Get-CimInstance -ClassName CIM_Memory } 
    '4' { Get-CimInstance -classname CIM_DiskDrive } 
    '5' { Get-CimInstance -classname CIM_Keyboard } 
    Default {  
        # Return will exit the process if there is incorrect input.
        return "not one of the options"
    }
}
