@echo off
setlocal
set "scriptDir=%~dp0"
set "scriptName=%~nx0"
set "platform=%~1"
if "%platform%"=="atcoder" goto atcoder
if "%platform%"=="leetcode" goto leetcode
goto usage

:atcoder
if "%~2"=="" goto usage
if not "%~4"=="" goto usage
shift
goto atcoder_setup

:leetcode
shift
set "problems="
set "language=py"
:parse
if "%~1"=="" goto create
if "%~1"=="py" goto language
if "%~1"=="cpp" goto language
echo(%~1| findstr /r /x "[0-9][0-9]*" >nul
if errorlevel 1 (
    echo Invalid problem number: %~1
    exit /b 1
)
set "number=%~1"
:strip_zero
if "%number:~0,1%"=="0" (
    set "number=%number:~1%"
    goto strip_zero
)
if not defined number (
    echo Problem numbers must be positive.
    exit /b 1
)
set "problems=%problems% %number%"
shift
goto parse

:language
set "language=%~1"
shift
if not "%~1"=="" goto usage

:create
if not defined problems goto usage
pushd "%scriptDir%.." || exit /b 1
for %%p in (%problems%) do (
    call :create_problem %%p
    if errorlevel 1 (
        popd
        exit /b 1
    )
)
popd
exit /b 0

:create_problem
set "number=%~1"
set "bucket=%number:~0,-2%"
if not defined bucket set "bucket=0"
set "bucket=%bucket%00"
set "target=src\leetcode\%bucket%\%number%"
if not exist "%target%" mkdir "%target%"
if not exist "%target%" exit /b 1
if exist "%target%\main.%language%" exit /b 0
type nul > "%target%\main.%language%"
exit /b %errorlevel%

:usage
echo Usage: %scriptName% atcoder abc425 [py^|cpp]
echo        %scriptName% leetcode number [number ...] [py^|cpp]
exit /b 1

:atcoder_setup
set "problemNo=%~1"
if not defined problemNo (
    echo Usage: %scriptName% atcoder abc425 [py^|cpp]
    exit /b 1
)
echo(%problemNo%| findstr /r /x "abc[0-9][0-9]* arc[0-9][0-9]* agc[0-9][0-9]* ahc[0-9][0-9]*" >nul
if errorlevel 1 (
    echo Invalid contest: %problemNo%
    exit /b 1
)
set "language=%~2"
if not defined language set "language=py"
if not "%language%"=="py" if not "%language%"=="cpp" (
    echo Invalid language: %language%. Use py or cpp.
    exit /b 1
)
set "category=%problemNo:~0,3%"
set "problems=a b c d e f"
if "%category%"=="abc" set "problems=a b c d e f g"
if "%category%"=="ahc" set "problems=a a_submit"
pushd "%scriptDir%.." || exit /b 1
call :atcoder_target
if not exist "%target%" mkdir "%target%"
if not exist "%target%" (
    popd
    exit /b 1
)
for %%p in (%problems%) do (
    if not exist "%target%\%%p.%language%" (
        call :atcoder_template_%language% > "%target%\%%p.%language%"
        if errorlevel 1 (
            popd
            exit /b 1
        )
    )
)
popd
endlocal
exit /b 0

:atcoder_target
set "number=%problemNo:~3%"
:atcoder_strip_zero
if "%number:~0,1%"=="0" (
    set "number=%number:~1%"
    goto atcoder_strip_zero
)
if not defined number set "number=0"
set /a "bucket=number / 100 * 100" >nul
if "%bucket%"=="0" set "bucket=000"
set "target=src\atcoder\%category%\%bucket%\%problemNo:~3%"
exit /b 0

:atcoder_template_py
echo def main():
echo     pass
echo.
echo if __name__ == '__main__':
echo     main()
exit /b 0

:atcoder_template_cpp
echo #include ^<iostream^>
echo.
echo using namespace std;
echo.
echo int main() {
echo     ios::sync_with_stdio(false);
echo     cin.tie(nullptr);
echo.
echo     return 0;
echo }
exit /b 0
