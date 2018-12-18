using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using VoidScribe;

namespace DebugEnviorment
{
    class Program
    {
        static void PrintResult(VoidScribeResult result)
        {
            Console.WriteLine(result.Data.ToString());
        }


        static void Main(string[] args)
        {
            VoidScribeRequest request = VoidScribeRequest.NameRequest("americanCities", 8);
            VoidScribeCallback callback = PrintResult;


            VoidScribeConnection.Request(callback, request);

            Console.ReadLine();
        }
    }
}
