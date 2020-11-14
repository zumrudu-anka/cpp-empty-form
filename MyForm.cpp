#include "MyForm.h"

using namespace System;
using namespace System::Windows::Forms;

[STAThreadAttribute]
int main(array<String^>^ args) {
	Application::EnableVisualStyles();
	Application::SetCompatibleTextRenderingDefault(false);
	EmptyForm::MyForm form;	// EmptyForm ifadesinin yerine proje adi yazilmali(X projesinin MyFormu gibi..MyForm ise olusturdugumuz formun adi)
	Application::Run(%form);
	return 0;
}
