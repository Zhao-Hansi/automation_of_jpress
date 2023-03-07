from selenium import webdriver
import time
import sys, getopt


def main(argv):
    '''
    命令行传参
    '''
    name = "firefox"

    try:
        opts, args = getopt.getopt(argv, "hn:", ["name="])
    except getopt.GetoptError:
        print('Error: ')
        print('   or: ')
        sys.exit(2)

    for opt, arg in opts:
        if opt == "-h":
            print('')
            print('or: ')
            sys.exit()
        elif opt in ("-n", "--name"):
            name = arg

    print('run browser name : %s' % name)
    return name


def browser(n=None):
    """
    启动浏览器, n是浏览器名称，支持浏览器：chrome ,firefox
    """

    if n == None:
        name = main(sys.argv[1:])
    else:
        name = n
    if name == "firefox":
        print("当前执行浏览器：%s" % name)
        return webdriver.Firefox()
    elif name == "chrome":
        print("当前执行浏览器：%s" % name)
        return webdriver.Chrome()
    else:
        print("支持浏览器：chrome,firefox")


if __name__ == "__main__":
    driver = browser()
    driver.get("http://localhost:8080/jpress/user/login")
    t = driver.title
    print(t)
    time.sleep(10)
    driver.quit()
