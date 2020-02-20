$basicList = @()
$tempList = @()
$i = 0
while($i-lt 10)
{
    $temp = 10 - $i
    #$input = Read-Host -prompt "Please enter  $temp  more things"
    $basicList += $i
    $i += 1 
}
if($basicList.Length -eq 10)
{
    Write-Host "Array has 10 items. True"
}
$one = $basicList[0]
$basicList[0] = $basicList[9]
$basicList[9] = $one
Write-Host "First 3"
Write-Host $basicList[0..2]
Write-Host "Last 3"
write-host $basicList[-3..-1]
Write-Host "Entire Array"
Write-Host $basiclist
if($basicList -contains "cat")
{
    Write-Host "Array has a Cat"
}
else
{
   Write-Host "Array Does not have a cat"
}
$marvel = Read-Host -Prompt "Please name your favorite marvel character "
$num = Get-random -Minimum 0 -Maximum 9
$basiclist[$num] = $marvel
Write-Host "The name: $marvel is at index $num"
Write-Host $basicList
$anotherarray = @()
for($i = 0; $i -lt $basicList.Length; $i++)
{
    try
    {
        $anotherarray += [int]$basicList[$i]
    }
    catch
    {
        continue
    }
}
$anotherarray = $anotherarray | sort
Write-Host $anotherarray
