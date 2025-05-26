import PyPDF2

class PDFExtractor:
    @staticmethod
    def extract_text(path: str) -> str:
        try:
            with open(path, "rb") as f:
                reader = PyPDF2.PdfReader(f)
                content = "\n".join(page.extract_text() for page in reader.pages if page.extract_text())
                print("content..........",content)
                return content
        except Exception as exc:
            print(f"[PDFExtractor] {path}: {exc}")
            return ""
