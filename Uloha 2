# ANSI Color Palette Generator

Tento PowerShell skript vykreslí paletu 16 standardních konzolových barev. Na rozdíl od nativních cmdletů PowerShellu řešení využívá nízkoúrovňové **ANSI escape sekvence**.

Skript demonstruje:
* Přímou práci s ANSI kódy pro formátování výstupu terminálu (`\033[<kód>m`).
* Matematický výpočet barev pozadí z barev popředí (kód pozadí je vždy kód popředí + 10).
* **Dynamický kontrast textu:** Algoritmus automaticky detekuje světlé/tmavé pozadí ve třetím sloupci a podle toho volí černou nebo zářivě bílou barvu písma pro zajištění maximální čitelnosti.

## Zdrojový kód (`Show-AnsiPalette.ps1`)

```powershell
<#
.SYNOPSIS
    Vykreslí paletu 16 barev pomocí ANSI escape sekvencí s dynamickým kontrastem.
#>

$colors = @(
    @{ Name = "Black";       Fg = 30 },
    @{ Name = "DarkBlue";    Fg = 34 },
    @{ Name = "DarkGreen";   Fg = 32 },
    @{ Name = "DarkCyan";    Fg = 36 },
    @{ Name = "DarkRed";     Fg = 31 },
    @{ Name = "DarkMagenta"; Fg = 35 },
    @{ Name = "DarkYellow";  Fg = 33 },
    @{ Name = "Gray";        Fg = 37 },
    @{ Name = "DarkGray";    Fg = 90 },
    @{ Name = "Blue";        Fg = 94 },
    @{ Name = "Green";       Fg = 92 },
    @{ Name = "Cyan";        Fg = 96 },
    @{ Name = "Red";         Fg = 91 },
    @{ Name = "Magenta";     Fg = 95 },
    @{ Name = "Yellow";      Fg = 93 },
    @{ Name = "White";       Fg = 97 }
)

# Escape znak (ASCII 27) pro inicializaci ANSI sekvence
$esc = [char]27

foreach ($c in$colors) {
    # Výpočet barvy pozadí (+10 dle ANSI standardu)
    $bg =$c.Fg + 10
    
    # Dynamický výběr barvy textu pro 3. sloupec:
    # Pokud je barva pozadí světlá (kód >= 90) nebo žlutá/šedá, použijeme černé písmo (30).
    # Pro tmavé barvy použijeme zářivě bílé písmo (97).
    $textColor = if ($c.Fg -ge 90 -or$c.Fg -in 33, 37) { 30 } else { 97 }
    
    # 1. sloupec - Výchozí text
    $col1 = "{0,-15}" -f $c.Name
    
    # 2. sloupec - Barva popředí
    $col2 = "$esc[{0}m{1,-20}$esc[0m" -f $c.Fg, $c.Name
    
    # 3. sloupec - Barva pozadí a dynamicky zvolená barva popředí
    $col3 = "$esc[{0};{1}m{2,-20}$esc[0m" -f $textColor, $bg,$c.Name
    
    Write-Host "$col1$col2$col3"
}
