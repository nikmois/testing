class Manufacturer:
    # конструктор - специальный метод с помощью которого производится
    # инициализация объекта
    #    def __init__(self):
    #        self.__ID = 0
    #        self.__Name = "NoName"
    #        self.__Country = "China"

    def __init__(self, ID=0, Name="NoName", Country="China"):
        self.__ID = ID
        self.__Name = Name
        self.__Country = Country

    def Print(self):
        print(f'ID: {self.__ID}')
        print(f'Name: {self.__Name}')
        print(f'Country: {self.__Country}')

    def SetID(self, ID: int):
        if not (type(ID) is int):
            raise TypeError
        if self.__ID < 0:
            raise ValueError
        self.__ID = ID

    def GetID(self) -> int:
        return self.__ID

    def SetName(self, Name: str):
        if not (type(Name) is str):
            raise TypeError
        if self.__Name == "":
            raise ValueError
        self.__Name = Name

    def GetName(self) -> str:
        return self.__Name

    def SetCountry(self, Country: str):
        if not (type(Country) is str):
            raise TypeError
        if self.__Country == "":
            raise ValueError
        self.__Country = Country

    def GetCountry(self) -> str:
        return self.__Country

    @staticmethod
    def ReadCsv(filename):
        manuf=[]

        lines=[]
        with open(filename, "r") as file:
            lines = file.read().splitlines()


        for line in lines:
            try:
                fields = line.split(",")
                m = Manufacturer(int(fields[0]), fields[1], fields[2])
                manuf.append(m)
            except:
                print("Line read error")

        return manuf

    @staticmethod
    def WriteHtml(filename, manufacturers):
        template = """<!doctype HTML>
        <html>
        <head>
        <title>Manufacturer list</title>
        <style>
            table,th,td {
            border: solid 1px black;
            border-collapse: collapse;
            }
            </style>
            </head>
            <body>
            <table>
            <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Country</th>
            </tr>
            {rows}
            </table>
            </body>
            </html>"""

        row_template = """<tr>
        <td>{id}</td>
        <td>{name}</td>
        <td>{country}</td>
        </tr>"""

        rows=""

        for m in manufacturers:
            row = row_template
            row = row.replace("{id}",str(m.GetID()))
            row = row.replace("{name}",m.GetName())
            row = row.replace("{country}",m.GetCountry())
            rows+=row

        template = template.replace("{rows}", rows)

        with open(filename, "w") as file:
            file.write(template)

#m = Manufacturer(0, "Name", "China")
#m2 = Manufacturer(1, "Intel", "USA")
#m.Print()
#m2.Print()

#m.SetID(2)
#print(m.GetID())

#m.SetName("Loli")
#print(m.GetName())

#m.SetCountry("Estonia")
#print(m.GetCountry())

manufs = Manufacturer.ReadCsv("Manufacturers.csv")

for manuf in manufs:
    manuf.Print()

Manufacturer.WriteHtml("manuf.html",manufs)
# m.ID=1
# m.Name="Intel"
# m.Counrtry="USA"

# m.Print()
