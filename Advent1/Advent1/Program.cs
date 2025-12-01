using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace Advent1
{
    class Program
    {
        static void Main(string[] args)
        {
            string path = "input.txt";
            string[] lines = File.ReadAllLines(path);

            int startval = 50;
            int actualvalue = 0;

            foreach (var line in lines)
            {
                char lettre = line.Substring(0,1).FirstOrDefault();
                int nombre = int.Parse(line.Substring(1));
                switch (lettre)
                {
                    case 'L':
                        {
                            startval -= nombre;
                            break;
                        }
                    case 'R':
                        {
                            startval += nombre;
                            break;
                        }
                    default:
                        { 
                            break;
                        }
                }

                while (startval >= 100) startval -= 100;
                while (startval < 0) startval += 100;

                if (startval == 0) actualvalue++;

            }

            Console.Write(actualvalue);
            Console.ReadLine();
        }
    }
}
