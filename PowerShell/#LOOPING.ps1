#LOOPING
# For this process i'm going to figure out what the variable of counter is.
# The counter will have a value of 1 and will only count up if it's -le 50
# Multiplier is for multiplying the intitial number
#$Factor = 2
$Factor=$true
$inputx = read-host -Prompt "Factor" 
$Factor = [int]$inputx
for ($counter = 1; $counter -le 50; $counter++){
    # The process below is how to write a multiplication statement as a command 
    $answer = $Factor * $counter
    # You have to set the write host in this process in order to make it look clean.
    Write-host "$factor * $counter = $answer"
}
# The next step is to make a pop up for when incorrect inputs are inserted by the user.
Catch{
    if ($Factor -isnot [int]){
        write-host "Use a proper integer" 
        $Factor=$false
    }
}