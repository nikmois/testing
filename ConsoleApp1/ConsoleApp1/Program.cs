using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    class Program
    {
        static void second(string[] args)
        {
            int a = 5;
            int b = 3;
            int c = a + b;

            string s = "123";
            s += ".";


            if (a > b)
            {
                Console.WriteLine($"{a} is greater than {b}");
            }

            for (int i = 1; i <= 5; i++)
            {
                Console.WriteLine(i);
            }

            int[] array = { 1, 2, 3, 4, 8, 9 };

            Console.WriteLine("The contents of n");
            foreach (int n in array)
            {
                Console.WriteLine(n);
            }

            Console.ReadKey();
        }
        static void Main(string[] args)
        {
            using (ChromeDriver driver = new ChromeDriver())
            {
                driver.Url = "http://localhost/testing/buttons.html";
                Console.WriteLine($"Page title: {driver.Title}");

                IWebElement div = driver.FindElementById("textBlock");
                if (div.Text.Length > 0)
                    Console.WriteLine("Error: #textBlock is not empty on a fresh page");
                var buttons = driver.FindElementsByTagName("button");

                foreach (IWebElement btn in buttons)
                {
                    string expected = btn.Text;
                    btn.Click();
                    string actual = div.Text;
                    Thread.Sleep(2000);
                    if (actual != expected)
                    { 
                        Console.WriteLine("Button click result mismatch.\n" +
                            $"\tExpected: {expected}\n\tActual: {actual}");
                    }
                }

                Thread.Sleep(15000);
            }

            

            Console.ReadKey();
        }
    }
}
