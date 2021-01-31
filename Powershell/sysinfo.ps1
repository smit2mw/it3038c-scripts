
#$ = "Hello, PowerShell!"
#write-Host($Hello)
function getIP {
    (Get-NetIPAddress).IPv4Address | Select-String "192*"
}

#write-host(getIP)
$IP = getIP
$User = $env:USERNAME
$HostName = hostname
$Power = $PSVersionTable.PSVersion | sort-object major | ForEach-Object {$_.major}
$Date = Get-Date -Format "dddd, MMMM, dd, yyyy"

$Body = "This Machine's IP is $IP. User is $User. Hostname is $HostName. PowerShell Version is $Power. Today's Date is $Date."
#Write-Host("This Machine's IP is $IP.") -NoNewline
#Write-Host("This Machine's IP is {0}" -f $IP)
# 
#write-host(" User is $User.") -NoNewline

#Write-Host(" Hostname is $HostName.") -NoNewline

#Write-Host(" PowerShell Version is $Power.") -NoNewline

#Write-Host(" Today's Date is $Date") 

write-host($Body)

#Send-MailMessage -To "silvercammel@gmail.com" -From "silvercammel@gmail.com" -Subject "IT3038c Windows Sysinfo" -Body $Body -SmtpServer smtp.google.com -port 587 -UseSsl -Credential (Get-Credential)