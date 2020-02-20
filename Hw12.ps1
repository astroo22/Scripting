$events = @{"Weezer"= @{"Jan 30; 2018"= @("Concrete Gold", "Etihad Stadium", "Melbourne, VIC");
                        "Jun 16; 2018"= @("Montebello Rockfest 2018"; "Montebello Marina";  "Montebello; QC")};
            "Tenacious D"= @{"May 06; 2018"= @("Shaky Knees Music Festival 2018"; "Central Park"; "Atlanta; GA");
                            "Jun 16; 2018"= @("Montebello Rockfest 2018"; "Montebello Marina"; "Montebello; QC")};
            "Lamb of God"= @{"Jun 09; 2018"= @("Final World Tour= North America 2018"; "Keybank Pavilion"; "Burgettstown; PA");
                            "Jun 16; 2018"= @("Montebello Rockfest 2018"; "Montebello Marina"; "Montebello; QC")};
            "Ed Sheeran"= @{"Mar 10; 2018"= @("Ed Sheeran with Missy Higgins"; "Etihad Stadium"; "Melbourne; VIC")};
            "Cold War Kids"= @{"Jun 02; 2018"= @("XFEST 2018"; "Keybank Pavilion"; "Burgettstown; PA")};
            "Steel Panther"= @{"Oct 21; 2017"= @("Aftershock"; "Discovery Park"; "Sacramento; CA")}} 

function addEvent()
{
    $d = @{}
    $dd = @{}
    $artist = Read-Host -Prompt "Artist or Band: "
    $concert = Read-Host -Prompt "Concert: "
    $date = Read-Host -Prompt "Date: "
    $venue = Read-Host -Prompt "Venue: "
    $location = Read-Host -Prompt "Location: "
    $l = @($concert,$venue,$loction)
    if($events.Containskey($artist))
    {
        $events[$artist] += @{$date=@($concert,$venue,$location)}

    }
    else
    {
        $events.add($artist,@{$date=@($concert,$venue,$location)})
    }

}
function printthing()
{
    foreach($band in $events.keys)
    {
        Write-Host "$band"
        foreach($date in $events[$band].keys)
        {
            Write-Host "`t $date"
            foreach($j in $events[$band][$date])
            {
                Write-Host "`t `t $j"
            }
        }
    }
}

$x = $true
while($x)
{
printthing
    $user = Read-Host -Prompt "Enter y if you would like to add more events or q to quit: "
    if($user -eq "y")
    {
        $y = $true
        while($y)
        {
            addevent
            printthing
            $ug = Read-Host -prompt "Would you like to add anymore? (y) for yes"
            if($ug -eq "y")
            {
                continue
            }
            else
            {
                $y = $false
                break
            }
        }
    }
    if($user -eq "q")
    {
        break
    }
}