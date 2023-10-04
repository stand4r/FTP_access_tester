from ftplib import FTP

logger = open('log.txt', 'a')
try:
    txt = open(input("File with sites: "), 'r')
except FileNotFoundError:
    print("Файл не найден")
    exit()
for i in txt.readlines():
    logger = open('log.txt', 'a')
    f = FTP()
    s = i.strip("\n").split(";")
    url, port = s[0].split(":", 1)
    port = int(port)
    login, passw = s[1].split(":", 1)
    logger.write(f"{url}:{port}:{login}:{passw}\n")
    print(f"\033[33mNow \033[37m-> {url}:{port}       {login}:{passw}")
    try:
        f.connect(host=url, port=port, timeout=10)
        f.login(login, passw)
        logger.write("Connection / Success\n")
        try:
            f.dir()
            logger.write("Dir / OK")
        except:
            logger.write("Dir / FAIL")
    except:
        logger.write("Connection / Fail\n")
    del f
    logger.write("\n\n")
    logger.close()
