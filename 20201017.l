%option noyywrap

%{
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

ofstream yyoutlog; // output filestream for log file

string loglist = ""; // list of tokens along with line numbers

int lines = 1; // to keep track of line numbers
%}

/* Regular Definitions */
delim [ \t\n]
ws {delim}+
newline [\r\n]

letter [a-zA-Z]
digit [0-9]

/* write regular expressions for id, float, and integers */
id {letter}({letter}|{digit}|_)*
number {digit}+

%%

{ws} { /* ignore whitespace */ }
{newline} {
    lines++;
}

"def" {
    loglist = "Line no " + to_string(lines) + ": Token <DEF> Lexeme " + yytext + " found\n"+ "\n";
    yyoutlog << loglist;
}

"range" {
    loglist = "Line no " + to_string(lines) + ": Token <RANGE> Lexeme " + yytext + " found\n" + "\n";
    yyoutlog << loglist;
}

"print" {
    loglist = "Line no " + to_string(lines) + ": Token <PRINT> Lexeme " + yytext + " found\n" + "\n";
    yyoutlog << loglist;
}

"for" {
    loglist = "Line no " + to_string(lines) + ": Token <FOR> Lexeme " + yytext + " found\n" + "\n";
    yyoutlog << loglist;
}


"if" {
    loglist = "Line no " + to_string(lines) + ": Token <IF> Lexeme " + yytext + " found\n" + "\n";
    yyoutlog << loglist;
}

"else" {
    loglist = "Line no " + to_string(lines) + ": Token <ELSE> Lexeme " + yytext + " found\n" + "\n";
    yyoutlog << loglist;
}

"return" {
    loglist = "Line no " + to_string(lines) + ": Token <RETURN> Lexeme " + yytext + " found\n" + "\n";
    yyoutlog << loglist;
}

"(" {
    loglist = "Line no " + to_string(lines) + ": Token <LPAREN> Lexeme " + yytext + " found\n" + "\n";
    yyoutlog << loglist;
}

")" {
    loglist = "Line no " + to_string(lines) + ": Token <RPAREN> Lexeme " + yytext + " found\n" + "\n";
    yyoutlog << loglist;
}

":" {
    loglist = "Line no " + to_string(lines) + ": Token <COLON> Lexeme " + yytext + " found\n" + "\n";
    yyoutlog << loglist;
}

"=" {
    loglist = "Line no " + to_string(lines) + ": Token <ASSIGNOP> Lexeme " + yytext + " found\n" + "\n";
    yyoutlog << loglist;
}

">" {
    loglist = "Line no " + to_string(lines) + ": Token <RELOP> Lexeme " + yytext + " found\n" + "\n";
    yyoutlog << loglist;
}

{id} {
    loglist = "Line no " + to_string(lines) + ": Token <ID> Lexeme " + yytext + " found\n" + "\n";
    yyoutlog << loglist;
}

{number} {
    loglist = "Line no " + to_string(lines) + ": Token <CONST_INT> Lexeme " + yytext + " found\n" + "\n";
    yyoutlog << loglist;
}
%%

int main(int argc, char* argv[]) {
    if (argc != 2) {
        cout << "Please input file name" << endl;
        return 0;
    }

    yyin = fopen(argv[1], "r");

    yyoutlog.open("my_log.txt", ios::trunc);

    if (yyin == NULL) {
        cout << "Error opening input file" << endl;
        return 0;
    }

    yylex();

    cout << "Total lines: " << lines << endl;

    yyoutlog << "Total lines: " << lines << endl;

    yyoutlog.close();

    fclose(yyin);

    return 0;
}
