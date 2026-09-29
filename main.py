from kivy.app import App
from kivy.uix.widget import Widget
from kivy.utils import platform
from kivy.core.window import Window

Window.fullscreen = 'auto'

URL = 'https://yyg.myfunmax.com/Pubg_Hack/index.html?st=13&miref=launcher'


class WebGameApp(App):
    def build(self):
        return Widget()

    def on_start(self):
        if platform != 'android':
            print("Ye sirf Android par chalega.")
            return

        from jnius import autoclass
        from android.runnable import run_on_ui_thread

        WebView = autoclass('android.webkit.WebView')
        WebViewClient = autoclass('android.webkit.WebViewClient')
        Activity = autoclass('org.kivy.android.PythonActivity').mActivity

        # FIX: webview ko reference me rakho warna Python garbage collect
        # kar dega aur app crash ho jayegi
        self.webview = None

        @run_on_ui_thread
        def create_webview():
            webview = WebView(Activity)
            settings = webview.getSettings()

            settings.setJavaScriptEnabled(True)
            settings.setDomStorageEnabled(True)
            settings.setLoadsImagesAutomatically(True)
            settings.setJavaScriptCanOpenWindowsAutomatically(True)
            settings.setMediaPlaybackRequiresUserGesture(False)
            settings.setAllowFileAccess(True)
            settings.setCacheMode(2)          # LOAD_CACHE_ELSE_NETWORK

            # FIX: WebViewClient ko subclass karo taaki links
            # browser me na khulein, webview ke andar hi chalein
            class MyWebViewClient(WebViewClient):
                def shouldOverrideUrlLoading(self, view, url):
                    view.loadUrl(str(url))
                    return True

            webview.setWebViewClient(MyWebViewClient())
            webview.loadUrl(URL)

            self.webview = webview           # strong reference
            Activity.setContentView(webview)

        create_webview()


if __name__ == '__main__':
    WebGameApp().run()
