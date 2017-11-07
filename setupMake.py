from credentials import INSTANCE_CONNECTION_NAME


def main():
    f = open("Makefile", 'a')
    sql = '"{}"=tcp:{}'.format(INSTANCE_CONNECTION_NAME, 3306)
    f.write(sql)
    f.close()
    print("Makefile updated!")


if __name__ == "__main__":
    main()
