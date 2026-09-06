"""Native Windows window for the existing local Studio, using WebView2."""
import ctypes
import logging
from pathlib import Path
import webview


def main():
    log_dir = Path(__file__).parent / 'data'
    log_dir.mkdir(exist_ok=True)
    logging.basicConfig(filename=log_dir / 'desktop.log', level=logging.INFO)
    try:
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('Auraly.Studio.Desktop')
        webview.create_window('Auraly Studio', 'http://127.0.0.1:8766',
                              width=1400, height=920, min_size=(1000, 700))
        webview.start(gui='edgechromium', private_mode=False,
                      storage_path=str(log_dir / 'desktop-profile'))
    except Exception:
        logging.exception('Falha ao abrir a janela do Studio')
        ctypes.windll.user32.MessageBoxW(None,
            'Não foi possível abrir a janela. Consulte studio/data/desktop.log.', 'Auraly Studio', 16)
        raise


if __name__ == '__main__':
    main()
