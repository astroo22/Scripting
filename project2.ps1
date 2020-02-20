cls

$desktopPath = "C:\Users\thoma\Desktop\"
$clientDataFolder = $desktopPath + "Client Data\"
$dataFolder = $clientDataFolder + "Data\"
$masterCSV = $dataFolder + "master.csv"
$masterInput

if (-not (Test-Path $clientDataFolder)){
    New-Item $clientDataFolder -ItemType "directory" | Out-Null
}

if (-not (Test-Path $dataFolder)){
    New-Item $dataFolder -ItemType "directory" | Out-Null
}

Set-Location $clientDataFolder

$regionList = @{
'NE'=@('CT','ME','VT','NH','MA','RI');
'MA'=@('NY','PA','NJ');
'ENC'=@('WI','IL','IN','OH','MI');
'WNC'=@('ND','SD','NE','KS','IA','MO','MN');
'SA'=@('FL','GA','SC','NC','VA','WV','MD','DC','DE');
'ESC'=@('KY','TN','MS','AL');
'WSC'=@('OK','TX','AR','LA');
'M'=@('NV','ID','MT','WY','CO','UT','AZ','NM');
'P'=@('CA','OR','WA','HI','AK')
}

Function Import(){
    CLS
    Write-Host "IMPORT"

    While($True){
        While($True){
            $fileName = Read-Host("Enter the full filename")
            if (Test-Path ($desktopPath + $fileName)){
                $file = $desktopPath + $fileName
                Write-Host $file
                break
            }else{
                Write-Host "File does not exist`r`n"
            }
        }
        $dataImport = Import-Csv $file -Type string,string,string,string,string,int,string,double,string

        if (-not (Test-Path $masterCSV)){
            $dataImport | Sort "Full Name" -unique | Export-CSV -NoTypeInformation $masterCSV
        }else{
            
            $temp = @()

            foreach($i in $masterInput){
                $client = [PSCustomObject]@{'Full Name'=$i.'Full Name'; 'CPhone1'=$i.CPhone1; 'caddress'=$i.caddress; 'ccity'=$i.ccity; 'cstate'=$i.cstate;
                        'czip'=$i.czip; 'dob'=$i.dob; 'salary'=$i.salary; 'Company'=$i.company}

                $temp += $client
            }
            
            foreach($i in $dataImport){
                $client = [PSCustomObject]@{'Full Name'=$i.'Full Name'; 'CPhone1'=$i.CPhone1; 'caddress'=$i.caddress; 'ccity'=$i.ccity; 'cstate'=$i.cstate;
                        'czip'=$i.czip; 'dob'=$i.dob; 'salary'=$i.salary; 'Company'=$i.company}
                
                $temp += $client
            }
            
            $temp | Sort "Full Name" -unique | Export-CSV -NoTypeInformation $masterCSV
        }

        $masterInput = Import-CSV $masterCSV

        $sel2 = Read-Host "Press a key to return to the main menu, enter to import another file"
        
        if($sel2 -eq ''){
            continue
        }else{
            CLS
            break
        }
    }
}

Function MainMenu(){
    While($True){
        if(Test-Path $masterCSV){
            $masterInput = Import-CSV $masterCSV
        }
        Write-Host "MAIN MENU"
        
        Write-Host "1.`tReports
2.`tPhone Directory
3.`tImport
4.`tDeletion
5.`tExit`r`n"

        $sel = Read-Host("Make your selection")

        # Really could have used a switch case here
        if ($sel -eq 1 -or $sel -eq 'reports'){
            REPORTS
        }elseif($sel -eq 2 -or $sel -eq 'phone directory'){
            PHONEDIRECTORY
        }elseif($sel -eq 3 -or $sel -eq 'import'){
            IMPORT
            Write-Host $file
        }elseif($sel -eq 4 -or $sel -eq 'deletion'){

        }elseif($sel -eq 5 -or $sel -eq 'exit'){
            break
        }else{
            cls
            Write-Host "[$sel] is not a valid input`r`n"
        }
    }
}

#region Reports
Function Reports(){
    CLS
    While($True){
        Write-Host "REPORTS MENU"
        
        Write-Host "1.`tClient Information
2.`tClient Salaries
3.`tClient Ages
4.`tAverage Salaries
5.`tReturn to Main Menu`r`n"

        $sel = Read-Host("Make your selection")

        # Really could have used a switch case here
        if ($sel -eq 1 -or $sel -eq 'info'){
            CLS
            CLIENTINFO
        }elseif($sel -eq 2 -or $sel -eq 'salaries'){
            CLIENTSALARIES
        }elseif($sel -eq 3 -or $sel -eq 'ages'){
            CLIENTAGES
        }elseif($sel -eq 4 -or $sel -eq 'average'){
            CLIENTAVERAGES
        }elseif($sel -eq 5 -or $sel -eq 'return'){
            CLS
            break
        }else{
            cls
            Write-Host "[$sel] is not a valid input`r`n"
        }
    }
}

Function ClientInfo(){
    if(-not (Test-Path $masterCSV)){
        Write-Host "No master loaded`r`n"
        break
    }

    CLS

    While($True){
        Write-Host "CLIENT INFORMATION REPORTS"
        Write-Host "List based on
1.`tCity
2.`tState
3.`tCompany
4.`tReturn to Main Menu"

        $sel = Read-Host "Make your selection"

        if($sel -eq 4 -or $sel -eq 'return'){
            break
        }

        Write-Host "`r`nDelivery Methods
1.`tDisplay
2.`tExport to CSV
3.`tBoth
4.`tCancel"

        $sel2 = Read-Host "Make your selection"

        if($sel2 -eq 4 -or $sel2 -eq 'exit'){
            continue
        }
        
        if($sel -eq 1 -or $sel -eq 'city'){
            $city = Read-Host "Enter a City"
            Write-Host

            $clientList = ($masterInput | Where-Object {$_.ccity -match $city})
            $clientExport = @()

            foreach($i in $clientList){
                $client = [PSCustomObject]@{'Full Name'=$i.'Full Name'; 'Company'=$i.company; 'salary'=$i.salary}
                $clientExport += $client
            }

            if($sel2 -eq 1 -or $sel2 -eq 'display'){
                CLS
                foreach($i in $clientList){
                    $sal = $i.salary
                    Write-Host $i.'Full Name', '-', $i.company, "- `$$sal"
                }
            }elseif($sel2 -eq 2 -or $sel2 -eq 'export'){
                $cityReport = $clientDataFolder + 'cityReport' + $city + '.csv'
                if (Test-Path $cityReport){
                    $sel3 = Read-Host "$cityReport already exists
Press any key to quit, enter to overwrite"
                    
                    if($sel3 -eq ''){
                        $clientExport | Export-CSV -NoTypeInformation $cityReport
                    }
                }
            }elseif($sel2 -eq 3 -or $sel2 -eq 'both'){
                CLS
                foreach($i in $clientList){
                    $sal = $i.salary
                    Write-Host $i.'Full Name', '-', $i.company, "- `$$sal"
                }
                
                $cityReport = $clientDataFolder + 'cityReport' + $city + '.csv'
                if (Test-Path $cityReport){
                    $sel3 = Read-Host "$cityReport already exists
Press any key to quit, enter to overwrite"
                    
                    if($sel3 -eq ''){
                        $clientExport | Export-CSV -NoTypeInformation $cityReport
                    }
                }
            }else{
                Write-Host "[$sel2] is not a valid input`r`n"
                continue
            }
            

        }elseif($sel -eq 2 -or $sel -eq 'state'){
            $state = Read-Host "Enter a State"
            Write-Host

            $clientList = ($masterInput | Where-Object {$_.cstate -match $state})
            $clientExport = @()

            foreach($i in $clientList){
                $client = [PSCustomObject]@{'Full Name'=$i.'Full Name'; 'Company'=$i.company; 'salary'=$i.salary}
                $clientExport += $client
            }

            if($sel2 -eq 1 -or $sel2 -eq 'display'){
                CLS
                foreach($i in $clientList){
                    $sal = $i.salary
                    Write-Host $i.'Full Name', '-', $i.company, "- `$$sal"
                }
            }elseif($sel2 -eq 2 -or $sel2 -eq 'export'){
                $stateReport = $clientDataFolder + 'stateReport' + $state + '.csv'
                if (Test-Path $stateReport){
                    $sel3 = Read-Host "$stateReport already exists
Press any key to quit, enter to overwrite"
                    
                    if($sel3 -eq ''){
                        $clientExport | Export-CSV -NoTypeInformation $stateReport
                    }
                }
            }elseif($sel2 -eq 3 -or $sel2 -eq 'both'){
                CLS
                foreach($i in $clientList){
                    $sal = $i.salary
                    Write-Host $i.'Full Name', '-', $i.company, "- `$$sal"
                }
                
                $stateReport = $clientDataFolder + 'stateReport' + $state + '.csv'
                if (Test-Path $stateReport){
                    $sel3 = Read-Host "$stateReport already exists
Press any key to quit, enter to overwrite"
                    
                    if($sel3 -eq ''){
                        $clientExport | Export-CSV -NoTypeInformation $stateReport
                    }
                }
            }else{
                Write-Host "[$sel2] is not a valid input`r`n"
                continue
            }

        }elseif($sel -eq 3 -or $sel -eq 'company'){
            $comp = Read-Host "Enter a Company"
            Write-Host

            $clientList = ($masterInput | Where-Object {$_.company -match $comp})
            $clientExport = @()

            foreach($i in $clientList){
                $client = [PSCustomObject]@{'Full Name'=$i.'Full Name'; 'Company'=$i.company; 'salary'=$i.salary}
                $clientExport += $client
            }

            if($sel2 -eq 1 -or $sel2 -eq 'display'){
                CLS
                foreach($i in $clientList){
                    $sal = $i.salary
                    Write-Host $i.'Full Name', '-', $i.company, "- `$$sal"
                }
            }elseif($sel2 -eq 2 -or $sel2 -eq 'export'){
                $companyReport = $clientDataFolder + 'companyReport' + $comp + '.csv'
                if (Test-Path $companyReport){
                    $sel3 = Read-Host "$companyReport already exists
Press any key to quit, enter to overwrite"
                    
                    if($sel3 -eq ''){
                        $clientExport | Export-CSV -NoTypeInformation $companyReport
                    }
                }
            }elseif($sel2 -eq 3 -or $sel2 -eq 'both'){
                CLS
                foreach($i in $clientList){
                    $sal = $i.salary
                    Write-Host $i.'Full Name', '-', $i.company, "- `$$sal"
                }
                
                $companyReport = $clientDataFolder + 'companyReport' + $comp + '.csv'
                if (Test-Path $companyReport){
                    $sel3 = Read-Host "$companyReport already exists
Press any key to quit, enter to overwrite"
                    
                    if($sel3 -eq ''){
                        $clientExport | Export-CSV -NoTypeInformation $companyReport
                    }
                }
            }else{
                Write-Host "[$sel2] is not a valid input`r`n"
                continue
            }
        }else{
            CLS
            Write-Host "[$sel] is not a valid input`r`n"
            continue
        }


        
        
    }
}


Function ClientSalaries(){
    if(-not (Test-Path $masterCSV)){
        Write-Host "No master loaded`r`n"
        break
    }

    While($True){
        CLS
        Write-Host "CLIENT SALARIES"

        $perc = Read-Host "Enter a salary percentage"
        $perc = [int]($masterInput.Count * ($perc / 100))
        
        foreach ($i in $masterInput | sort salary -Descending | Select-Object -First $perc){
            Write-Host $i
        }
        #Write-Host $masterInput
        Read-Host
    }
}

Function ClientAges(){

}

Function ClientAverages(){

}
#endregion Reports

#region Phone Directory
Function PhoneDirectory(){
    CLS
    While($True){
        Write-Host "PHONE DIRECTORY"
        
        Write-Host "1.`tClient Lookup
2.`tList by State
3.`tList by Company
4.`tList by Region
5.`tReturn to Main Menu`r`n"

        $sel = Read-Host("Make your selection")

        # Really could have used a switch case here
        if ($sel -eq 1 -or $sel -eq 'lookup'){
            LOOKUP
        }elseif($sel -eq 2 -or $sel -eq 'state'){
            STATELOOKUP
        }elseif($sel -eq 3 -or $sel -eq 'company'){
            COMPANYLOOKUP
        }elseif($sel -eq 4 -or $sel -eq 'region'){
            REGIONLOOKUP
        }elseif($sel -eq 5 -or $sel -eq 'return'){
            CLS
            break
        }else{
            CLS
            Write-Host "[$sel] is not a valid input`r`n"
        }
    }
}

Function Lookup(){
    if(-not (Test-Path $masterCSV)){
        Write-Host "No master loaded`r`n"
        break
    }

    While($True){
        CLS
        Write-Host "CLIENT LOOKUP"
        
        $name = Read-Host "Enter a client's name"
        Write-Host

        $clientList = ($masterInput | Where-Object {$_.'Full Name' -match $name})

        foreach ($client in $clientList){

            $fullName = $client.'Full Name'
            $phone = $client.CPhone1
            $address = $client.caddress
            $city = $client.ccity
            $state = $client.cstate
            $zip = $client.czip
            $company = $client.company

            Write-Host "$fullName 
Phone Number: $phone,
Address: $address, $city, $state, $zip
$company`r`n"
        }

        $sel2 = Read-Host "Press a key to return to the main menu, enter to look up another client"
        
        if($sel2 -eq ''){
            continue
        }else{
            CLS
            break
        }
    }
}

Function StateLookup(){
    if(-not (Test-Path $masterCSV)){
        Write-Host "No master loaded`r`n"
        break
    }

    

    While($True){
        CLS
        Write-Host "STATE LOOKUP"
        $state = Read-Host "Enter a State Abbreviation"
        Write-Host

        $clientList = ($masterInput | Where-Object {$_.cstate -eq $state})

        foreach ($client in $clientList){

            $fullName = $client.'Full Name'
            $phone = $client.CPhone1
            $address = $client.caddress
            $city = $client.ccity
            $state = $client.cstate
            $zip = $client.czip
            $company = $client.company

            Write-Host "$fullName 
Phone Number: $phone,
Address: $address, $city, $state, $zip
$company`r`n"
        }

        $sel2 = Read-Host "Press a key to return to the main menu, enter to look up another state"
        
        if($sel2 -eq ''){
            continue
        }else{
            CLS
            break
        }
    }
}

Function CompanyLookup(){
    if(-not (Test-Path $masterCSV)){
        Write-Host "No master loaded`r`n"
        break
    }

    While($True){
        CLS
        Write-Host "COMPANY LOOKUP"
        $comp = Read-Host "Enter a Company"
        Write-Host

        $clientList = ($masterInput | Where-Object {$_.company -match $comp})

        foreach ($client in $clientList){

            $fullName = $client.'Full Name'
            $phone = $client.CPhone1
            $address = $client.caddress
            $city = $client.ccity
            $state = $client.cstate
            $zip = $client.czip
            $company = $client.company

            Write-Host "$fullName 
Phone Number: $phone,
Address: $address, $city, $state, $zip
$company`r`n"
        }

        $sel2 = Read-Host "Press a key to return to the main menu, enter to look up another state"
        
        if($sel2 -eq ''){
            continue
        }else{
            CLS
            break
        }
    }
}

Function RegionLookup(){
    if(-not (Test-Path $masterCSV)){
        Write-Host "No master loaded`r`n"
        break
    }

    While($True){
        CLS
        Write-Host "REGION LOOKUP"

        Write-Host "`tRegion List
`t1.`tNew England [NE]
`t2.`tMid-Atlantic [MA]
`t3.`tEast North Central [ENC]
`t4.`tWest North Central [WNC]
`t5.`tSouth Atlantic [SA]
`t6.`tEast South Central [ESC]
`t7.`tWest South Central [WSC]
`t8.`tMountain [M]
`t9.`tPacific [P]"
        

        $region = Read-Host "`r`nEnter a Region (use abbreviation)"
        Write-Host

        $clientList = ($masterInput | Where-Object {$regionList.$region -contains $_.cstate})

        foreach ($client in $clientList){

            $fullName = $client.'Full Name'
            $phone = $client.CPhone1
            $address = $client.caddress
            $city = $client.ccity
            $state = $client.cstate
            $zip = $client.czip
            $company = $client.company

            Write-Host "$fullName 
Phone Number: $phone,
Address: $address, $city, $state, $zip
$company`r`n"
        }

        $sel2 = Read-Host "Press a key to return to the main menu, enter to look up another region"
        
        if($sel2 -eq ''){
            continue
        }else{
            CLS
            break
        }
    }
}
#endregion Phone Directory

Function Run(){
    Write-Host "Welcome!`r`n"

    if (-not (Test-Path $masterCSV)){
        Write-Host "No master loaded`r`n"
    }else{
        Write-Host "Master loaded at $masterCsv`r`n"
        $masterInput = Import-CSV $masterCSV
    }

    MAINMENU

    CLS
    Write-Host "Thank you for choosing TLewis Consulting!"
}

Run