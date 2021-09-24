using Microsoft.VisualStudio.TestTools.UnitTesting;
using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using OpenQA.Selenium.Interactions;
using OpenQA.Selenium.Support.UI;
using System;
using System.Threading;

namespace SeleniumUnitTests
{
    /*[TestClass]
    public class ButtonsTest
    {
        // Единый драйвер для всех тестов
        static ChromeDriver driver = null;

        // Инициализация драйвера при запуске набора тестов
        [ClassInitialize]
        public static void Setup(TestContext ctx)
        {
            if (driver == null)
                driver = new ChromeDriver();
        }

        // Высвобождение 
        [ClassCleanup]
        public static void Cleanup()
        {
            driver.Dispose();
        }

        [TestMethod]
        public void PageTitleTest()
        {
            driver.Url = "http://localhost/testing/buttons.html";
            Assert.AreEqual("Buttons", driver.Title);
        }

        [TestMethod]
        public void ButtonClickTest()
        {
            driver.Url = "http://localhost/testing/buttons.html";
            //Console.WriteLine($"Page title: {driver.Title}");

            IWebElement div = driver.FindElementById("textBlock");

            Assert.AreEqual(0, div.Text.Length);

            //Console.WriteLine("Error: #textBlock is not empty on a fresh page");

            var buttons = driver.FindElementsByTagName("button");

            foreach (IWebElement btn in buttons)
            {
                string expected = btn.Text;
                btn.Click();
                string actual = div.Text;
                Assert.AreEqual(expected, actual);
            }
        }
    }*/

    [TestClass]
    public class BooksTest
    {
        // Единый драйвер для всех тестов
        static ChromeDriver driver = null;

        // Инициализация драйвера при запуске набора тестов
        [ClassInitialize]
        public static void Setup(TestContext ctx)
        {
            if (driver == null)
                driver = new ChromeDriver();
        }

        // Высвобождение 
        [ClassCleanup]
        public static void Cleanup()
        {
            driver.Dispose();
        }

        [TestMethod]
        public void BookSelectTest()
        {
            driver.Url = "http://localhost/testing/books/books.html";
            Thread.Sleep(1000);

            // Найти на странице элемент с id="#book-select"
            IWebElement select = driver.FindElementById("book-select");
            // Внутри него найти все элементы вида <option>
            var options = select.FindElements(By.TagName("option"));
            // Убедиться, что <option> ровно 4 штуки
            Assert.AreEqual(4, options.Count);
            // Убедиться, что первый <option> содержит ожидаемый текст
            // <option>The C++ Programming Language</option>
            Assert.AreEqual("The C++ Programming Language", options[0].Text);
            // <option value="1">The C++ Programming Language</option>
            Assert.AreEqual("1", options[0].GetAttribute("value"));
        }


        // Задание:
        // Сделать тест, выбирающий из списка конкретную запись,
        // нажимающий на кнопку "Получить данные"
        // И проверяющий, что в нужное место добавляется <ul>
        // В котором содержатся <li>, в которых содержится текст
        [TestMethod]
        public void SelectOptionTest()
        {
            driver.Url = "http://localhost/testing/books/books.html";
            Thread.Sleep(100);
            IWebElement select = driver.FindElementById("book-select");

            SelectElement sel = new SelectElement(select);
            sel.SelectByValue("3");

            var buttons = driver.FindElementsById("select-button");

            foreach (IWebElement btn in buttons)
            {
                btn.Click();
            }
            Thread.Sleep(5000);

            /*IWebElement option = select.FindElement(
            By.CssSelector("#book-select option[value='3']"));

            var options_xpath = driver.FindElements(
                By.XPath("/html/body/div[@id='main']/div[@class='main-header']/" +
                "/div[@class='main-headertext']/select[@id='book-select']/option"));*/

            /*Actions builder = new Actions(driver);
            IAction chain = builder.MoveToElement(select).Click().
                MoveToElement(option).Click().Build();

            chain.Perform();*/
            var lists = driver.FindElementByClassName("main-bookinfo");
            var unlists = lists.FindElements(By.TagName("ul"));
            Assert.AreEqual(3, unlists.Count);

        }
    }
}
