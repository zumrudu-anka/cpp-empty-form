#include "MyForm.h"

using namespace System;
using namespace System::Windows::Forms;

[STAThreadAttribute]
int main(array<String^>^ args) {
	Application::EnableVisualStyles();
	Application::SetCompatibleTextRenderingDefault(false);
	// Tr // MyProjectName ifadesinin yerine proje adi yazilmali(X projesinin MyFormu gibi..MyForm ise olusturdugumuz formun adi)
	// En // Replace MyProjectName with the name of your Project.(Like MyForm of XProject..MyForm is the name of the Form you created)
	MyProjectName::MyForm form;
	Application::Run(%form);
	return 0;
}
