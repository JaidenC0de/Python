Clear-Host
# To start with getting the date of the week for M, T, R, and F i'm going to get the date of today.
# After I get the date the next step is to make variables that go with the day of the week.
$date = (get-date).DayOfWeek
# An array with variables representing representing days of week
$Days = @($m, $t, $w, $t, $f, $sat, $sun)
$Days["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
# The next step is to write write host to say what "School days" for all the days of the week except wednesday
if ($date -eq $W) {
    Write-Host "Online"
    # Wednesdays are supposed will say school is "Online"
} 
# When Elseif statement =
elseif ($Date -eq $sat -or $Date -eq $Sun) {
    Write-host "Remote"
}
# The else statment will write-host when 
else {
    Write-Host "School day"
}