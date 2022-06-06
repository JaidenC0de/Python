#for ($num = 1; $num -le 25; $num++) {
#    "file_" + $num + ".txt"
#}
#$answer = read-host "enter yes or no"
#$answer  = $answer.ToLower
#if ($answer -eq "yes") {
#    write-host $answer
#}
#-----------------------------------------
#foreach($variable in get-content $othervariable) 
#$changed = "$nowtime" + "" + "ALTERED: " +$Variable
function get-version {
    $PSVersionTable.PSVersion
}