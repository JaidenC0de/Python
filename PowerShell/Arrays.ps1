#------------------example------------------------
#$a=1,2
#$a | Get-Member
#$sampleArray = @(1, 2, 3, 4)
#------------------attachment 1-------------------
#$hooligans  = @("Jaiden,", "Johnny,", "Jazz")
#$ages = @("17,", "10,", "2")
#write-host "$hooligans are ages: $ages"
# -----------------attachment 2-------------------
# I want to make an array that will measure how much somebody who works either a full week or parts of a week would make.
$Employees = @('Derick', 'Eddy', 'grant')
$employees[0, 1, 2]
$pay 
for ($counter = 1; $counter -le 5; $counter++) {
    $income = $pay * $counter
    write-host $pay * $counter = $income
}