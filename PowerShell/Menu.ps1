# Below is what is intitially shown to the user so they know the function different choices.
write-host "-----------PBJ Menu------------" -foreground blue
write-host "1 - Peanut                     " 
Write-host "2 - Butter                     " 
write-host "3 - Jelly                      " 
Write-host "press anything else to Quit    " -foreground red 
$select = Read-host "please choose an option" 
switch ($select)
{
    '1' {'You chose Peanut'} 
    '2' {'You chose Butter'} 
    '3' { 'You chose Jelly'} 
    '123' {"It's Peaunt Butter Jelly Time!"} 
    Default {  
        return 'Bye, have a beautiful time.' 
        # I want to make it so the return option will return the user to the original list after putting in a wrong input.
    }
}
{}