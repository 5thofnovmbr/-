// dllmain.cpp : DLL 애플리케이션의 진입점을 정의합니다.
#include "pch.h"
// 다른 헤더들을 pch.h에 include해서 사용하는 것 같다.
#include "windows.h"
#include "tchar.h"
#include "Urlmon.h"
/*
windows.h: 윈도우즈 기반 프로그래밍시 필수
tchar.h: 유니코드와 아스키코드 둘 다 사용할 때 필요(TCHAR <- wchar_t 자료형 선언)
shlobj.h: DriveType, GetFileNameFromBrowse 등의 기능
Wininet.h: cache와 관련된듯..(https://docs.microsoft.com/en-us/windows/win32/api/wininet/)
*/

#pragma comment(lib, "Urlmon.lib")
/*
 전처리기.
 #prgma comment( comment-type, comment string? )
 comment type :  compiler, exestr, lib, linker, user
 명시적인 라이브러리 링크
 #pragma comment(lib, "Mylib.lib")

 Win32인터넷 함수 사용을 위해 밑 두개가 필요
 #include <wininet.h>
 #pragma comment(lib, "wininet.lib")

 Wininet.lib API로 FTP연결
 */

#define DEF_URL L"https://www.google.com/index.html"
#define DEF_FILE_NAME L"index.html"
 /*
 L은 wchar_t
 보통 영문 알파벳은 1바이트인데 유니코드는 2바이트 이상이어서 wchar_t에 저장
 */

HMODULE g_hMod = NULL;

DWORD WINAPI ThreadProc(LPVOID lparam)
{
    /*
     lpvoid == void*
     == long point void 어떠한 타입으로도 변환가능
     LPVOID형의 변수를 lparam이라는 식별자로 선언한것
     */
    TCHAR szPath[MAX_PATH] = { 0, };    // MAX_PATH==260(경로길이) systme32폴더

    if (!GetModuleFileName(g_hMod, szPath, MAX_PATH))
        return FALSE;

    TCHAR *p = _tcsrchr(szPath, '\\');  //szPath에서 \를 찾아 인덱스(주소?)반환
    /*
        _tcsrchr은 strrchr에 대응하는 TCHAR용 함수
        문자찾기(문자열끝에서부터 검색)
        지금은 szPath에서 유니코드 \를 찾고있음
        해당 문자의 주소를 리턴 = p
        */
    if (!p)
        return FALSE;  //p가 없으면 거짓반환

    _tcscpy_s(p + 1, MAX_PATH, DEF_FILE_NAME);
    /*
        _tcscpy_s 주 사용목적: BOF방지, 잘못된 메모리 연산 방지
        _tcscpy_s(저장변수, 쓰려는 데이터크기+1, 쓰려고 하는 데이터);
        if문 조건이 실행되면 p에 \이 있는 주소(인덱스)가 저장되고 인덱스+1을
        DEF_INDEX_FILE에 복사??
        */
    
    URLDownloadToFile(NULL, DEF_URL, szPath, 0, NULL);
    /*
    Urlmon.lib을 호출했는데도 식별자를 못찾겠다고 한다.
    --> Urlmon.h도 include 시켜야한다.
    */
    return 0;
}

/* 
BOOL: ↓ 반환값이 Boolean인 함수 
WINAPI: 함수호출규약(__stdcall, __cdecl 등)지정 __stdcall로 지정한다.
WINAPI, APIENTRY, CALLBACK는 다 __stdcall으로 지정
*/
BOOL WINAPI DllMain(HMODULE hModule,
    DWORD  ul_reason_for_call,
    LPVOID lpReserved
)
{
    HANDLE hThread = NULL;
    
    g_hMod = (HMODULE)hModule;

    switch (ul_reason_for_call)
    {
    case DLL_PROCESS_ATTACH:
        OutputDebugString(L"dll injection...");
        hThread = CreateThread(NULL, 0, ThreadProc, NULL, 0, NULL);
        CloseHandle(hThread);
        break;
    }
    return TRUE;
}

#ifdef __cplusplus
extern "C" {
#endif
    __declspec(dllexport) void dummy()
    {
        return;
    }
#ifdef __cplusplus
}
#endif

// dll을 기초부터 공부해야겠다.
