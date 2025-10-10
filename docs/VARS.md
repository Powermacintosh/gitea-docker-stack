# Пользовательский интерфейс - Метаданные (ui.meta)

AUTHOR: Gitea - Git with a cup of tea: Author meta tag of the homepage.
DESCRIPTION: Gitea (Git with a cup of tea) is a painless self-hosted Git service written in Go: Description meta tag of the homepage.
KEYWORDS: go,git,self-hosted,gitea: Keywords meta tag of the homepage.

# Безопасность (security)

MIN_PASSWORD_LENGTH: 8: Минимальная длина пароля для новых пользователей.

PASSWORD_CHECK_PWN: false: Проверьте HaveIBenPwned, чтобы узнать, был ли раскрыт пароль.

# Камуфляж (camo)

ENABLED: false: Включите медиа-прокси, на данный момент мы поддерживаем только изображения.
SERVER_URL: пустой: URL-адрес камуфляжного сервера, требуется, если включен камуфляж.
HMAC_KEY: пусто: Укажите ключ HMAC для кодирования URL-адресов, он требуется, если камуфляж включен.
ALWAYS: false: Set to true to use camo for both HTTP and HTTPS content, otherwise only non-HTTPS URLs are proxied. ALLWAYS is deprecated and will be removed in a future release.

# Клиент OAuth2 (oauth2_client)

REGISTER_EMAIL_CONFIRM: [service] REGISTER_EMAIL_CONFIRM: Set this to enable or disable email confirmation of OAuth2 auto-registration. (Overwrites the REGISTER_EMAIL_CONFIRM setting of the [service] section)
OPENID_CONNECT_SCOPES: empty: List of additional openid connect scopes. (openid is implicitly added)
ENABLE_AUTO_REGISTRATION: false: Автоматически создавайте учетные записи пользователей для новых пользователей oauth2.
USERNAME: никнейм: Источник имени пользователя для новых учетных записей oauth2:
userid- используйте атрибут userid / sub
nickname- используйте прозвище
preferred_username- используйте preferred_username
email- используйте часть имени пользователя атрибута электронной почты
Note: nickname, preferred_username and email options will normalize input strings using the following criteria:
Диакритики удалены
the characters in the set ['´`] are removed
the characters in the set [\s~+] are replaced with -
UPDATE_AVATAR: false: Обновите аватар, если он доступен у провайдера oauth2. Обновление будет выполняться при каждом входе в систему.
ACCOUNT_LINKING: логин: Как справиться, если учетная запись / электронная почта уже существует:
отключено - показать ошибку
логин - показать учетную запись, связывая логин
auto - автоматически связывается с учетной записью (Пожалуйста, имейте в виду, что это предоставит доступ к существующей учетной записи только потому, что указано одно и то же имя пользователя или адрес электронной почты. Вы должны убедиться, что это не вызовет проблем с вашими поставщиками аутентификации.)

# Сервис (service)

ACTIVE_CODE_LIVE_MINUTES: 180: Time limit (min) to confirm account/email registration.

RESET_PASSWD_CODE_LIVE_MINUTES: 180: Time limit (min) to confirm forgot password reset process.

REGISTER_EMAIL_CONFIRM: false: Включите эту опцию, чтобы запросить подтверждение регистрации по электронной почте. Требуется включить Mailer.

REGISTER_MANUAL_CONFIRM: false: Включите эту опцию, чтобы вручную подтверждать новые регистрации. Требуется отключить REGISTER_EMAIL_CONFIRM.

DISABLE_REGISTRATION: false: Отключите регистрацию, после чего только администратор может создавать учетные записи для пользователей.

REQUIRE_EXTERNAL_REGISTRATION_PASSWORD: false: Включите это, чтобы заставить созданные извне учетные записи (через GitHub, OpenID Connect и т. д.) создавать пароль.

ПРЕДУПРЕЖДЕНИЕ
Включение этого снизит безопасность, поэтому вы должны включить его только в том случае, если знаете, что делаете.
REQUIRE_SIGNIN_VIEW: false: Включите это, чтобы заставить пользователей войти в систему для просмотра любой страницы или использования API. Его можно установить на "дорогой", чтобы заблокировать анонимных пользователей доступ к некоторым страницам, которые потребляют много ресурсов, например: заблокировать анонимным сканерам ИИ от доступа к кодовым страницам репозитория. «Дорогой» режим является экспериментальным и может быть изменен.

ENABLE_NOTIFY_MAIL: false: Включите это, чтобы отправлять электронное письмо наблюдателям репозитория, когда что-то происходит, например, создавая проблемы. Требуется включение Mailer.

ENABLE_BASIC_AUTHENTICATION: true: Отключите это, чтобы отразить аутентификацию с использованием HTTP BASIC и пароля пользователя. Обратите внимание, что если вы отключите это, вы не сможете получить доступ к конечным точкам API токенов с помощью пароля. Кроме того, это отключает только базовую аутентификацию с использованием пароля, а не токенов или OAuth Basic.

ENABLE_PASSWORD_SIGNIN_FORM: true: Show the password login form (for password-based login), otherwise, only show OAuth2 or passkey login methods if they are enabled. If you set it to false, maybe it also needs to set ENABLE_BASIC_AUTHENTICATION to false to completely disable password-based authentication.

ENABLE_PASSKEY_AUTHENTICATION: true: Разрешить пользователям войти в систему с помощью ключа доступа

ENABLE_REVERSE_PROXY_AUTHENTICATION: false: Включите это, чтобы разрешить обратную аутентификацию прокси для веб-запросов

ENABLE_REVERSE_PROXY_AUTHENTICATION_API: false: Включите это, чтобы разрешить обратную прокси-аутентификацию для запросов API, обратный прокси отвечает за то, чтобы CSRF не был возможен.

ENABLE_REVERSE_PROXY_AUTO_REGISTRATION: false: Включите это, чтобы разрешить автоматическую регистрацию для обратной аутентификации.

ENABLE_REVERSE_PROXY_EMAIL: false: Включите это, чтобы разрешить автоматическую регистрацию с предоставленным адресом электронной почты, а не сгенерированным адресом электронной почты.

ENABLE_REVERSE_PROXY_FULL_NAME: false: Включите это, чтобы разрешить автоматическую регистрацию с предоставленным полным именем пользователя.

ENABLE_CAPTCHA: false: Включите это, чтобы использовать проверку капчи для регистрации.

REQUIRE_CAPTCHA_FOR_LOGIN: false: Включите это, чтобы потребовать проверку captcha для входа в систему. Вы также должны включить ENABLE_CAPTCHA.

REQUIRE_EXTERNAL_REGISTRATION_CAPTCHA: false: Включите это, чтобы принудительно проверить капчу даже для внешних учетных записей (т.е. GitHub, OpenID Connect и т. д.). Вы также должны включить ENABLE_CAPTCHA.

CAPTCHA_TYPE: изображение: [изображение, recaptcha, hcaptcha, mcaptcha, cfturnstile]

RECAPTCHA_SECRET: "": Перейдите по ссылке https://www.google.com/recaptcha/admin, чтобы узнать секрет для recaptcha.

RECAPTCHA_SITEKEY: "": Перейдите по ссылке https://www.google.com/recaptcha/admin, чтобы получить ключ сайта для recaptcha.

RECAPTCHA_URL: https://www.google.com/recaptcha/: Установите URL-адрес recaptcha - позволяет использовать сеть recaptcha.

HCAPTCHA_SECRET: "": Зарегистрируйтесь на https://www.hcaptcha.com/, чтобы получить секрет для hcaptcha.

HCAPTCHA_SITEKEY: "": Зарегистрируйтесь на https://www.hcaptcha.com/, чтобы получить ключ сайта для hcaptcha.

MCAPTCHA_SECRET: "": Перейдите в свой экземпляр mCaptcha, чтобы получить секрет для mCaptcha.

MCAPTCHA_SITEKEY: "": Перейдите в свой экземпляр mCaptcha, чтобы получить ключ сайта для mCaptcha.

MCAPTCHA_URL https://demo.mcaptcha.org/: Установите URL-адрес mCaptcha.

CF_TURNSTILE_SECRET "": Перейдите по ссылке https://dash.cloudflare.com/? to=/:account/turnstile, чтобы получить секрет для turntile cloudflare.

CF_TURNSTILE_SITEKEY "": Перейдите по ссылке https://dash.cloudflare.com/? to=/:account/turnstile, чтобы получить ключ сайта для turntile cloudflare.

DEFAULT_KEEP_EMAIL_PRIVATE: false: По умолчанию пользователи должны сохранять конфиденциальное адрес электронной почты.

DEFAULT_ALLOW_CREATE_ORGANIZATION: true: Разрешить новым пользователям создавать организации по умолчанию.

DEFAULT_USER_IS_RESTRICTED: false: По умолчанию предоставлять новым пользователям ограниченные разрешения

DEFAULT_ENABLE_DEPENDENCIES: true: Включите это, чтобы зависимости были включены по умолчанию.

ALLOW_CROSS_REPOSITORY_DEPENDENCIES: true Включите это, чтобы разрешить зависимости от проблем из любого репозитория, где пользователю предоставляется доступ.

USER_LOCATION_MAP_URL: "": URL-адрес картографической службы для отображения местоположения пользователя на карте. Местоположение будет добавлено к URL-адресу в качестве параметра экранного запроса.

ENABLE_USER_HEATMAP: true: Включите это, чтобы отображать тепловую карту в профилях пользователей.

ENABLE_TIMETRACKING: true: Включить функцию отслеживания времени.

DEFAULT_ENABLE_TIMETRACKING: true: Разрешить репозиториям использовать отслеживание времени по умолчанию.

DEFAULT_ALLOW_ONLY_CONTRIBUTORS_TO_TRACK_TIME: true: Разрешить отслеживать время только пользователям с разрешениями на запись.

EMAIL_DOMAIN_ALLOWLIST: пусто: Если не пусто, разделено запятыми список доменных имен, которые могут быть использованы только для регистрации в этом экземпляре, поддерживается подстановочный знак.

EMAIL_DOMAIN_BLOCKLIST: пустой: Если не пустой, разделенный запятыми список доменных имен, которые не могут быть использованы для регистрации в этом экземпляре, поддерживается подстановочный знак.

SHOW_REGISTRATION_BUTTON: ! DISABLE_REGISTRATION: Показать кнопку регистрации

SHOW_MILESTONES_DASHBOARD_PAGE: true Включите это, чтобы ототозвить страницу панели управления вехами - представление всех вех пользователя

AUTO_WATCH_NEW_REPOS: true: Включите это, чтобы все пользователи организации смотрели новые репозитории при их создании

AUTO_WATCH_ON_CHANGES: false: Включите это, чтобы пользователи смотрели репозиторий после первого включения в него

DEFAULT_USER_VISIBILITY: public: Установите режим видимости по умолчанию для пользователей, либо "публичный", "ограниченный" или "частный".

ALLOWED_USER_VISIBILITY_MODES: публичный,ограниченный,приватный: Установите, какие режимы видимости может иметь пользователь

DEFAULT_ORG_VISIBILITY: public: Установите режим видимости по умолчанию для организаций, либо "публичный", "ограниченный" или "частный".

DEFAULT_ORG_MEMBER_VISIBLE: false True сделает членство пользователей видимым при добавлении в организацию.

ALLOW_ONLY_INTERNAL_REGISTRATION: false Установите значение true для принудительной регистрации только через Gitea.

ALLOW_ONLY_EXTERNAL_REGISTRATION: false Установите значение true, чтобы принудительно зарегистрироваться только с использованием сторонних сервисов.

NO_REPLY_ADDRESS: noreply.DOMAIN Значение для доменной части адреса электронной почты пользователя в журнале Git, если пользователь установил KeepEmailPrivate в true. DOMAIN разрешает значение в server.DOMAIN. Электронная почта пользователя будет заменена на конкатенацию имени пользователя в нижнем регистре, "@" и NO_REPLY_ADDRESS.

USER_DELETE_WITH_COMMENTS_MAX_TIME: 0 Минимальное количество времени, в течение которого пользователь должен существовать, прежде чем комментарии будут сохранены при удалении пользователя.

VALID_SITE_URL_SCHEMES: http, https: Действительные схемы URL-адресов сайта для профилей пользователей

# Сервис - Исследуйте (service.explore)

REQUIRE_SIGNIN_VIEW: false: Разрешить только зарегистрированным пользователям просматривать страницы исследования.
DISABLE_USERS_PAGE: false: Отключите страницу исследования пользователей.
DISABLE_ORGANIZATIONS_PAGE: false: Отключите страницу исследования организаций.
DISABLE_CODE_PAGE: false: Отключите страницу исследования кода.

# Запрос на качество обслуживания (qos)

ENABLED: false: Включить запрос на качество обслуживания и защиту от перегрузки.
MAX_INFLIGHT: (динамический): Максимальное количество параллельных запросов, которые сервер обработает перед поставкой новых запросов в чередь. По умолчанию "CpuNum \* 4".
MAX_WAITING: 100: Максимальное количество запросов, которые могут быть помести в очередь до того, как новые запросы будут отброшены.
TARGET_WAIT_TIME: 250 мс: Целевое максимальное время ожидания, для запроса может быть в очереди. Запросы, которые стоят в очереди менее этого периода времени, не будут отброшены. Когда время ожидания превышает эту сумму, часть запросов будет отброшена до тех пор, пока время ожидания не уменьшится ниже этой суммы.

# Минимальные размеры ключей SSH (ssh.minimum_key_sizes)

Определите разрешенные алгоритмы и их минимальную длину ключа (используйте -1 для отключения типа):

ED25519: 256
ECDSA: 256
RSA: 3071: Мы устанавливаем здесь 3071, потому что действительный ключ 3072 RSA может быть зарегистрирован как длина 3071.
DSA: -1: DSA теперь отключен по умолчанию. Установите на 1024 для повторного всего вогна, но убедитесь, что вам, возможно, придется перенастроить вашего поставщика SSHD

# Почтовый (mailer)

ПРЕДУПРЕЖДЕНИЕ
Этот раздел для Gitea 1.18 и более поздних. Если вы используете Gitea 1.17 или более раней строй, пожалуйста, обратитесь к примеру Gitea 1.17 app.ini и документу конфигурации Gitea 1.17
ENABLED: false: Разрешить использование почтовой службы.
PROTOCOL: empty: Mail server protocol. One of "smtp", "smtps", "smtp+starttls", "smtp+unix", "sendmail", "dummy". Before 1.18, this was inferred from a combination of MAILER_TYPE and IS_TLS_ENABLED.
Семейство SMTP, если ваш провайдер явно не говорит, какой протокол он использует, но предоставляет порт, вы можете установить SMTP_PORT вместо этого, и это будет выводится.
sendmail Use the operating system's sendmail command instead of SMTP. This is common on Linux systems.
манекен Отправить сообщения электронной почты в журнал в качестве этапа тестирования.
Note that enabling sendmail will ignore all other mailer settings except ENABLED, FROM, SUBJECT_PREFIX and SENDMAIL_PATH.
Enabling dummy will ignore all settings except ENABLED, SUBJECT_PREFIX and FROM.
SMTP_ADDR: empty: Mail server address. e.g. smtp.gmail.com. For smtp+unix, this should be a path to a unix socket instead. Before 1.18, this was combined with SMTP_PORT under the name HOST.
SMTP_PORT: empty: Mail server port. If no protocol is specified, it will be inferred by this setting. Common ports are listed below. Before 1.18, this was combined with SMTP_ADDR under the name HOST.
25: небезопасный SMTP
465: SMTP Secure
587: Запуск TLS
USE_CLIENT_CERT: false: Используйте сертификат клиента для TLS/SSL.
CLIENT_CERT_FILE: custom/mailer/cert.pem: Файл сертификата клиента.
CLIENT_KEY_FILE: custom/mailer/key.pem: Файл ключа клиента.
FORCE_TRUST_SERVER_CERT: false: Если установлено значение true, полностью игнорирует ошибки проверки сертификата сервера. Этот вариант небезопасен. Вместо этого рассмотрите возможность добавления сертификата в хранилище доверия к системе.
USER: пусто: Имя пользователя почтового пользователя (обычно адрес электронной почты отправителя).
PASSWD: пусто: Пароль пользователя электронной почты. Используйте «ваш пароль» для кавычек, если вы используете специальные символы в пароле.
Обратите внимание: аутентификация поддерживается только тогда, когда связь SMTP-сервера зашифрована с помощью TLS (это может быть через STARTTLS) или SMTP-хост является локальным хостом. См. раздел Настройка электронной почты для получения дополнительной информации.
ENABLE_HELO: true: Включить операцию HELO.
HELO_HOSTNAME: (извлет из системы): имя хоста HELO.
FROM: пусто: Почта с адреса, RFC 5322. Это может быть просто адрес электронной почты или формат «Имя» \<email@example.com\>.
ENVELOPE_FROM: пусто: Адрес, установленный как адрес От в почтовом конверте SMTP. Установите <>, чтобы отправить пустой адрес.
FROM_DISPLAY_NAME_FORMAT: {{ .DisplayName }}: If gitea sends mails on behave of users, it will just use the name also displayed in the WebUI. If you want e.g. Mister X (by CodeIt) <gitea@codeit.net>, set it to {{ .DisplayName }} (by {{ .AppName }}). Available Variables: .DisplayName, .AppName and .Domain.
SUBJECT_PREFIX: пусто: Префикс должен быть размещен перед строками темы электронной почты.
SENDMAIL_PATH: sendmail: Расположение sendmail в операционной системе (может быть командным или полным путем).
SENDMAIL_ARGS: empty: Specify any extra sendmail arguments. (NOTE: you should be aware that email addresses can look like options - if your sendmail command takes options you must set the option terminator --)
SENDMAIL_TIMEOUT: 5m: тайм-аут по умолчанию для отправки электронной почты через sendmail
SENDMAIL_CONVERT_CRLF: правда: Большинство версий sendmail предпочитают окончания строк LF, а не строки CRLF. Установите значение false, если ваша версия sendmail требует окончания строки CRLF.
SEND_BUFFER_LEN: 100: Buffer length of mailing queue. DEPRECATED use LENGTH in [queue.mailer]
SEND_AS_PLAIN_TEXT: false: Отправляйте письма только в виде обычного текста, без альтернативы HTML.
EMBED_ATTACHMENT_IMAGES: false: Встраивайте прилагаемые изображения в формате base64 в HTML-электронные письма. (для клиентов, которые не загружают внешние изображения, или отключенных пользователей vpn, которые все еще получают электронные письма; ВНИМАНИЕ: онлайн-веб-клиенты, такие как gmail, не будут показывать встроенные изображения base64)

# Изображение (picture)

GRAVATAR_SOURCE: gravatar: Can be gravatar, duoshuo or anything like http://cn.gravatar.com/avatar/.

DISABLE_GRAVATAR: false: Включите это, чтобы использовать только локальные аватары. УСТАРЕВШЕЕ [v1.18+] перемещено в базу данных. Используйте панель администратора для настройки.

ENABLE_FEDERATED_AVATAR: false: Включить поддержку федеративных аватаров (см. http://www.libravatar.org). УСТАРЕВШЕЕ [v1.18+] перемещено в базу данных. Используйте панель администратора для настройки.

AVATAR_STORAGE_TYPE: default: Storage type defined in [storage.xxx]. Default is default which will read [storage] if no section [storage] will be a type local.

AVATAR_UPLOAD_PATH: данные/аватары: Путь к хранению файлов изображений аватара пользователя.

AVATAR_MAX_WIDTH: 4096: Максимальная ширина изображения аватара в пикселях.

AVATAR_MAX_HEIGHT: 4096: Максимальная высота изображения аватара в пикселях.

AVATAR_MAX_FILE_SIZE: 1048576 (1MiB): Максимальный размер файла изображения аватара в байтах.

AVATAR_MAX_ORIGIN_SIZE: 262144 (256 КиБ): Если загруженный файл не превышает этот размер байта, изображение будет использоваться как есть, без измения размера/конвертирования.

AVATAR_RENDERED_SIZE_FACTOR: 2: Коэффициент умножения для визуализирных изображений аватаров. Большие значения приводят к более точному рендерингу на устройствах HiDPI.

REPOSITORY_AVATAR_STORAGE_TYPE: default: Storage type defined in [storage.xxx]. Default is default which will read [storage] if no section [storage] will be a type local.

REPOSITORY_AVATAR_UPLOAD_PATH: data/repo-avatars: Путь к хранению файлов изображений аватаров репозитория.

REPOSITORY_AVATAR_FALLBACK: нет: Как Gitea справляется с отсутствующими аватарами репозитория

нет = аватар не будет отображаться
random = будет сгенерирован случайный аватар
изображение = будет использоваться изображение по умолчанию (которое установлено в REPOSITORY_AVATAR_FALLBACK_IMAGE)
REPOSITORY_AVATAR_FALLBACK_IMAGE: /img/repo_default.png: Image used as default repository avatar (if REPOSITORY_AVATAR_FALLBACK is set to image and none was uploaded)

# Журнал (log)

ROOT_PATH: пусто: Корневой путь для файлов журналов.
MODE: консоль: Режим вхи. Для нескольких режимов используйте запятую для разделения значений. Вы можете настроить каждый режим в подразделах журнала каждого режима \[log.writer-mode-name\]
LEVEL: Информация: Общий уровень журнала. [Трассовка, Отладка, Информация, Предупреждение, Ошибка, Критический, Фатальный, Нет]
STACKTRACE_LEVEL: Нет: Уровень журнала по умолчанию, на котором можно зарегистрировать создание следов стека (редко полезно, не устанавливайте его). [Трассовка, Отладка, Информация, Предупреждение, Ошибка, Критический, Фатальный, Нет]
ENABLE_SSH_LOG: false: сохранить журнал ssh в файл журнала
logger.access.MODE: пусто: Регистратор "доступа"
logger.router.MODE: ,: Регистратор "маршрутизатора", одна запятая означает, что он будет использовать режим по умолчанию выше
logger.xorm.MODE: ,: Регистратор "xorm"

# Журнал доступа (log)

ACCESS_LOG_TEMPLATE: {{.Ctx.RemoteHost}} - {{.Identity}} {{.Start.Format "[02/Jan/2006:15:04:05 -0700]" }} "{{.Ctx.Req.Method}} {{.Ctx.Req.URL.RequestURI}} {{.Ctx.Req.Proto}}" {{.ResponseWriter.Status}} {{.ResponseWriter.Size}} "{{.Ctx.Req.Referer}}" "{{.Ctx.Req.UserAgent}}": Sets the template used to create the access log.
Доступны следующие переменные:
Ctx: the context.Context of the request.
Identity: the SignedUserName or "-" if not logged in.
Start: время начала запроса.
ResponseWriter: ответWriter из запроса.
RequestID: значение, соответствующее REQUEST_ID_HEADERS (по умолчанию: -, если не соответствует).
Вы должны быть очень осторожны, чтобы убедиться, что этот шаблон не выдает ошибок или паники, так как этот шаблон работает вне сценария паники/восстановления.
REQUEST_ID_HEADERS: пусто: Здесь можно настроить несколько значений, разделенных запятыми. Он будет соответствовать порядку конфигурации, и первое совпадение, наконец, будет напечатано в журнале доступа.
например
В заголовке запроса: X-Request-ID: test-id-123
Конфигурация в app.ini: REQUEST_ID_HEADERS = X-Request-ID
Печать в журнале: 127.0.0.1:58384 - - [14 февраля/2023:16:33:51 +0800] "test-id-123" ...

# Подразделы журнала (log.<writer-mode-name>)

MODE: имя: Устанавливает режим этого журнала - По умолчанию предоставляется имя предоставленного подраздела. Это позволяет иметь два разных файловых регистратора на разных уровнях.
LEVEL: log.LEVEL: Sets the log-level of this writer. Defaults to the LEVEL set in the global [log] section.
STACKTRACE_LEVEL: log.STACKTRACE_LEVEL: Устанавливает уровень журнала, на котором должны быть зарегистрированы трассы стека.
EXPRESSION: "": Регулярное выражение, соответствующее имени функции, файлу или сообщению. По умолчанию пусто. В регистраторе будут сохранены только сообщения журнала, соответствующие выражению.
FLAGS: stdflags: A comma separated string representing the log flags. Defaults to stdflags which represents the prefix: 2009/01/23 01:23:23 ...a/b/c/d.go:23:runtime.Caller() [I]: message. none means don't prefix log lines. See modules/log/flags.go for more information.
PREFIX: "": Дополнительный префикс для каждой строки журнала в этом регистраторе. По умолчанию пусто.
COLORIZE: false: Следует ли раскрашивать строки журнала

# Режим журнала консоли (log.console, или MODE=console)

For the console logger COLORIZE will default to true if not on windows or the terminal is determined to be able to color.
STDERR: false: Используйте Stderr вместо Stdout.
File log mode (log.file, or MODE=file)

FILE_NAME: Set the file name for this logger. Defaults to gitea.log (exception: access log defaults to access.log). If relative will be relative to the ROOT_PATH
LOG_ROTATE: true: Поверните файлы журналов.
MAX_SIZE_SHIFT: 28: Максимальный сдвиг размера одного файла, 28 означает 256 Мб.
DAILY_ROTATE: true: Вращайте журналы ежедневно.
MAX_DAYS: 7: Удалить файл журнала через n дней
COMPRESS: true: Сжимайте старые файлы журналов по умолчанию с помощью gzip
COMPRESSION_LEVEL: -1: Уровень сжатия

# Режим журнала Conn (log.conn, или MODE=conn)

RECONNECT_ON_MSG: false: Повторно подключите хост для каждого сообщения.
RECONNECT: false: Попробуйте восстановить подключение при потере соединения.
PROTOCOL: tcp: Установите протокол, либо "tcp", "unix", либо "udp".
ADDR: :7020: Устанавливает адрес для подключения.

# Гит (git)

PATH: "": Путь к исполняемому файлу Git. Если пусто, Gitea выполняет поиск в среде PATH.
HOME_PATH: {APP_DATA_PATH}/home: The HOME directory for Git. This directory will be used to contain the .gitconfig and possible .gnupg directories that Gitea's git calls will use. If you can confirm Gitea is the only application running in this environment, you can set it to the normal home directory for Gitea user.
DISABLE_DIFF_HIGHLIGHT: false: Отключает выделение добавленных и удаленных изменений.
MAX_GIT_DIFF_LINES: 1000: Максимально допустимое количество строк одного файла в другом представлении.
MAX_GIT_DIFF_LINE_CHARACTERS: 5000: Максимальное количество символов на строку, выделенную в другом представлении.
MAX_GIT_DIFF_FILES: 100: Максимальное количество файлов, отображаемых в другом представлении.
COMMITS_RANGE_SIZE: 50: Установите размер диапазона фиксации по умолчанию
BRANCHES_RANGE_SIZE: 20: Установите размер диапазона ветвей по умолчанию
GC_ARGS: empty: Аргументы для команды git gc, например --aggressive --auto. Смотрите больше на http://git-scm.com/docs/git-gc/
ENABLE_AUTO_GIT_WIRE_PROTOCOL: true: If use Git wire protocol version 2 when Git version >= 2.18, default is true, set to false when you always want Git wire protocol version 1. To enable this for Git over SSH when using a OpenSSH server, add AcceptEnv GIT_PROTOCOL to your sshd_config file.
PULL_REQUEST_PUSH_MESSAGE: true: Отвечать на push-файлы в не-ветку по умолчанию с URL-адресом для создания Pull Request (если они включены в репозитории)
VERBOSE_PUSH: true: Печать информации о статусе push-изов по мере их обработки.
VERBOSE_PUSH_DELAY: 5s: Печатайте подробное внимание только в том случае, если нажатие занимает больше времени, чем эта задержка.
LARGE_OBJECT_THRESHOLD: 1048576: (только Go-Git), не кэшируйте объекты больше этого в памяти. (Установите 0, чтобы отключить.)
DISABLE_CORE_PROTECT_NTFS: false Set to true to forcibly set core.protectNTFS to false.
DISABLE_PARTIAL_CLONE: false Отключите использование частичных клонов для git.

# OAuth2 (oauth2)

ENABLED: true: Включает провайдера OAuth2.
ACCESS_TOKEN_EXPIRATION_TIME: 3600: Срок службы токена доступа OAuth2 в секундах
REFRESH_TOKEN_EXPIRATION_TIME: 730: Срок службы токена обновления OAuth2 в часах
INVALIDATE_REFRESH_TOKENS: false: Проверьте, был ли уже использован токен обновления
JWT_SIGNING_ALGORITHM: RS256: Algorithm used to sign OAuth2 tokens. Valid values: [HS256, HS384, HS512, RS256, RS384, RS512, ES256, ES384, ES512]
JWT_SECRET: empty: OAuth2 authentication secret for access and refresh tokens, change this to a unique string. This setting is only needed if JWT_SIGNING_ALGORITHM is set to HS256, HS384 or HS512.
JWT_SECRET_URI: пусто: Вместо определения JWT_SECRET в конфигурации, этот параметр конфигурации может быть использован для предоставления Gitea пути к файлу, содержащему секрет (пример значения:file:/etc/gitea/oauth2_jwt_secret)
JWT_SIGNING_PRIVATE_KEY_FILE: jwt/private.pem: Private key file path used to sign OAuth2 tokens. The path is relative to APP_DATA_PATH. This setting is only needed if JWT_SIGNING_ALGORITHM is set to RS256, RS384, RS512, ES256, ES384 or ES512. The file must contain a RSA or ECDSA private key in the PKCS8 format. If no key exists a 4096 bit key will be created for you.
MAX_TOKEN_LENGTH: 32767: Максимальная длина токена/куки для принятия от поставщика OAuth2
DEFAULT_APPLICATIONS: git-credential-oauth, git-credential-manager, tea: Предварительная регистрация приложений OAuth для некоторых сервисов при запуске. Список доступных опций см. в документации OAuth2.

# Сервер (server)

APP_DATA_PATH: AppWorkPath/data: Это корневой путь по умолчанию для хранения данных.

PROTOCOL: http: [http, https, fcgi, http+unix, fcgi+unix]

Примечание: Значение должно быть в нижнем регистре.
USE_PROXY_PROTOCOL: false: Ожидайте заголовки протокола PROXY на соединениях

PROXY_PROTOCOL_TLS_BRIDGING: false: Когда протокол https, ожидайте заголовки протокола PROXY после согласования TLS.

PROXY_PROTOCOL_HEADER_TIMEOUT: 5s: Тайм-аут для ожидания заголовка протокола PROXY (установлено в 0, чтобы не было тайм-аута)

PROXY_PROTOCOL_ACCEPT_UNKNOWN: false: Принимайте заголовки протокола PROXY с неизвестным типом.

DOMAIN: localhost: Доменное имя этого сервера.

ROOT_URL: {PROTOCOL}://{DOMAIN}:{HTTP_PORT}/: Перезапишите автоматически сгенерированный публичный URL. Это полезно, если внутренний и внешний URL-адрес не совпадают (например, за обратным прокси-сервером).

PUBLIC_URL_DETECTION: legacy: Контролирует, как генерировать публичный URL-адрес. Хотя по умолчанию используется "устарение" (чтобы избежать разрыва существующих пользователей), большинство экземпляров должны использовать "автоматическое" поведение, особенно когда требуется доступ к экземпляру Gitea в контейнерной сети.

"legacy": сгенерируйте публичный URL-адрес с помощью заголовка "Host", если заголовок "X-Forwarded-Proto" существует, в противном случае используйте "ROOT_URL".
"auto": всегда используйте заголовок "Host", а также используйте заголовок "X-Forwarded-Proto", если он существует. Если нет заголовка "Host", используйте "ROOT_URL".
STATIC_URL_PREFIX: empty: Overwrite this option to request static resources from a different URL. This includes CSS files, images, JS files and web fonts. Avatar images are dynamic resources and still served by Gitea. The option can be just a different path, as in /static, or another domain, as in https://cdn.example.com. Requests are then made as {ROOT_URL}/static/assets/css/index.css or https://cdn.example.com/assets/css/index.css respectively. The static files are located in the public/ directory of the Gitea source repository. You can proxy the STATIC_URL_PREFIX requests to Gitea server to serve the static assets, or copy the manually built Gitea assets from $GITEA_BUILD/public to the assets location, eg: /var/www/assets, make sure $STATIC_URL_PREFIX/assets/css/index.css points to /var/www/assets/css/index.css.

ПРИМЕЧАНИЕ
Вы должны отключить ui.notification.EVENT_SOURCE_UPDATE_TIME, установив его в -1. Если вы этого не сделаете, некоторые элементы пользовательского интерфейса не будут работать. Вы получите следующую ошибку в консоли браузера Uncaught SecurityError: Failed to construct 'SharedWorker'.
HTTP_ADDR: 0.0.0.0: HTTP-адрес прослушивания.

If PROTOCOL is set to fcgi, Gitea will listen for FastCGI requests on TCP socket defined by HTTP_ADDR and HTTP_PORT configuration settings.
If PROTOCOL is set to http+unix or fcgi+unix, this should be the name of the Unix socket file to use. Relative paths will be made absolute against the AppWorkPath.
HTTP_PORT: 3000: HTTP-порт прослушивания.

If PROTOCOL is set to fcgi, Gitea will listen for FastCGI requests on TCP socket defined by HTTP_ADDR and HTTP_PORT configuration settings.
UNIX_SOCKET_PERMISSION: 666: Разрешения для сокета Unix.

LOCAL_ROOT_URL: {PROTOCOL}://{HTTP_ADDR}:{HTTP_PORT}/: Local (DMZ) URL for Gitea workers (such as SSH update) accessing web service. In most cases you do not need to change the default value. Alter it only if your SSH server node is not the same as HTTP node. For different protocol, the default values are different. If PROTOCOL is http+unix, the default value is http://unix/. If PROTOCOL is fcgi or fcgi+unix, the default value is {PROTOCOL}://{HTTP_ADDR}:{HTTP_PORT}/. If listen on 0.0.0.0, the default value is {PROTOCOL}://localhost:{HTTP_PORT}/, Otherwise the default value is {PROTOCOL}://{HTTP_ADDR}:{HTTP_PORT}/.

LOCAL_USE_PROXY_PROTOCOL: {USE_PROXY_PROTOCOL}: При создании локальных соединений проходит заголовок протокола PROXY. Это должно быть установлено на false, если локальное соединение будет проходить через прокси.

PER_WRITE_TIMEOUT: 30 с: Время истекает для любой записи на соединение. (Установлите -1, чтобы отключить все тайм-ауты.)

PER_WRITE_PER_KB_TIMEOUT: 10s: Тайм-аут на Кб, записанный на соединения.

DISABLE_SSH: false: Отключите функцию SSH, когда она недоступна.

START_SSH_SERVER: false: Если включено, используйте встроенный SSH-сервер.

SSH_SERVER_USE_PROXY_PROTOCOL: false: Ожидайте заголовок протокола PROXY при подключении к встроенному SSH-серверу.

BUILTIN_SSH_SERVER_USER: {RUN_USER}: Имя пользователя для встроенного SSH-сервера.

SSH_USER: {BUILTIN_SSH_SERVER_USER}: SSH username displayed in clone URLs. If it is set to (DOER_USERNAME), it will use current signed-in user's username. This option is only for some advanced users who have configured their SSH reverse-proxy and need to use different usernames for git SSH clone. Most users should just leave it blank and/or modify the BUILTIN_SSH_SERVER_USER.

SSH_DOMAIN: {DOMAIN}: Доменное имя этого сервера, используемое для отображаемого URL-адреса клона.

SSH_PORT: 22: порт SSH отображается в URL-адресе клона.

SSH_LISTEN_HOST: 0.0.0.0: Адрес прослушивания для встроенного SSH-сервера.

SSH_LISTEN_PORT: {SSH_PORT}: Порт для встроенного SSH-сервера.

SSH_ROOT_PATH: ~/.ssh: Корневой путь каталога SSH.

SSH_CREATE_AUTHORIZED_KEYS_FILE: true: Gitea создаст файл authorized_keys по умолчанию, когда он не использует внутренний сервер ssh. Если вы собираетесь использовать функцию AuthorizedKeysCommand, вы должны отключить ее.

SSH_AUTHORIZED_KEYS_BACKUP: false: Включить авторизованное резервное копирование ключей SSH при перезаписи всех ключей, по умолчанию false.

SSH_TRUSTED_USER_CA_KEYS: empty: Specifies the public keys of certificate authorities that are trusted to sign user certificates for authentication. Multiple keys should be comma separated. E.g.ssh-<algorithm> <key> or ssh-<algorithm> <key1>, ssh-<algorithm> <key2>. For more information see TrustedUserCAKeys in the sshd config man pages. When empty no file will be created and SSH_AUTHORIZED_PRINCIPALS_ALLOW will default to off.

SSH_TRUSTED_USER_CA_KEYS_FILENAME: RUN_USER/.ssh/gitea-trusted-user-ca-keys.pem: Absolute path of the TrustedUserCaKeys file Gitea will manage. If you're running your own ssh server and you want to use the Gitea managed file you'll also need to modify your sshd_config to point to this file. The official docker image will automatically work without further configuration.

SSH_AUTHORIZED_PRINCIPALS_ALLOW: off or username, email: [off, username, email, anything]: Specify the principals values that users are allowed to use as principal. When set to anything no checks are done on the principal string. When set to off authorized principal are not allowed to be set.

SSH_CREATE_AUTHORIZED_PRINCIPALS_FILE: false/true: Gitea will create a authorized_principals file by default when it is not using the internal ssh server and SSH_AUTHORIZED_PRINCIPALS_ALLOW is not off.

SSH_AUTHORIZED_PRINCIPALS_BACKUP: false/true: Enable SSH Authorized Principals Backup when rewriting all keys, default is true if SSH_AUTHORIZED_PRINCIPALS_ALLOW is not off.

SSH_AUTHORIZED_KEYS_COMMAND_TEMPLATE: {{.AppPath}} --config={{.CustomConf}} serv key-{{.Key.ID}}: Set the template for the command to passed on authorized keys. Possible keys are: AppPath, AppWorkPath, CustomConf, CustomPath, Key - where Key is a models/asymkey.PublicKey and the others are strings which are shellquoted.

SSH_SERVER_CIPHERS: chacha20-poly1305@openssh.com, aes128-ctr, aes192-ctr, aes256-ctr,aes128-gcm@openssh.com, aes256-gcm@openssh.com: Для встроенного SSH-сервера выберите шифры для поддержки SSH-соединений, для системного SSH эта настройка не влияет.

SSH_SERVER_KEY_EXCHANGES: curve25519-sha256, ecdh-sha2-nistp256, ecdh-sha2-nistp384, ecdh-sha2-nistp521, diffie-hellman-group14-sha256, diffie-hellman-group14-sha1: Для встроенного SSH-сервера выберите алгоритмы обмена ключами для поддержки SSH-соединений, для системного SSH эта настройка не влияет.

SSH_SERVER_MACS: hmac-sha2-256-etm@openssh.com, hmac-sha2-256, hmac-sha1: Для встроенного сервера SSH выберите MAC для поддержки SSH-соединений, для системного SSH эта настройка не влияет

SSH_SERVER_HOST_KEYS: ssh/gitea.rsa, ssh/gogs.rsa: For the built-in SSH server, choose the keypairs to offer as the host key. The private key should be at SSH_SERVER_HOST_KEY and the public SSH_SERVER_HOST_KEY.pub. Relative paths are made absolute relative to the APP_DATA_PATH. If no key exists a 4096 bit RSA key will be created for you.

SSH_KEY_TEST_PATH: /tmp: Каталог для создания временных файлов при тестировании открытых ключей с использованием ssh-keygen, по умолчанию это временный каталог системы.

SSH_KEYGEN_PATH: empty: Use ssh-keygen to parse public SSH keys. The value is passed to the shell. By default, Gitea does the parsing itself.

SSH_EXPOSE_ANONYMOUS: false: Включить экспозицию URL-адреса клона SSH для анонимных посетителей, по умолчанию false.

SSH_PER_WRITE_TIMEOUT: 30с: Время выхода для любой записи в SSH-соединения. (Установлите -1, чтобы отключить все тайм-ауты.)

SSH_PER_WRITE_PER_KB_TIMEOUT: 10 с: Тайм-аут на Кб, записанный на SSH-соединения.

MINIMUM_KEY_SIZE_CHECK: true: Укажите, нужно ли проверять минимальный размер клавиши с соответствующим типом.

OFFLINE_MODE: true: Отключает использование CDN для статических файлов и Gravatar для изображений профиля.

CERT_FILE: https/cert.pem: Путь к файлу Cert, используемый для HTTPS. При цепочке сначала должен быть сертификат сервера, а затем промежуточные сертификаты ЦС (если таковые есть). Это игнорируется, если ENABLE_ACME=true. Пути относятся к CUSTOM_PATH.

KEY_FILE: https/key.pem: Путь к файлу ключа, используемый для HTTPS. Это игнорируется, если ENABLE_ACME=true. Пути относятся к CUSTOM_PATH.

STATIC_ROOT_PATH: StaticRootPath: Верхний уровень шаблона и путь к статическим файлам.

APP_DATA_PATH: данные (/data/gitea на docker): Путь по умолчанию для данных приложения. Относительные пути будут абсолютными против AppWorkPath.

STATIC_CACHE_TIME: 6h: Web browser cache time for static resources on custom/, public/ and all uploaded avatars. Note that this cache is disabled when RUN_MODE is "dev".

ENABLE_GZIP: false: Включить сжатие gzip для контента, сгенерируемого во время выполнения, статические ресурсы исключены.

ENABLE*PPROF: false: Application profiling (memory and cpu). For "web" command it listens on localhost:6060. For "serv" command it dumps to disk at PPROF_DATA_PATH as (cpuprofile|memprofile)*<username>\_<temporary id>

PPROF_DATA_PATH: AppWorkPath/data/tmp/pprof: PPROF_DATA_PATH, используйте абсолютный путь при запуске Gitea как сервис

LANDING_PAGE: главная страница: Целевая страница для неаутентифицированных пользователей [home, explore, organizations, login,custom]. Где пользователь вместо этого будет любым URL-адресом, таким как "/org/repo" или дажеhttps://anotherwebsite.com

LFS_START_SERVER: false: Включает поддержку Git LFS.

LFS_ALLOW_PURE_SSH: false: Включает поддержку протокола Git LFS Pure SSH. В настоящее время отключен по умолчанию, см. Поддержка Git LFS.

LFS_CONTENT_PATH: {APP_DATA_PATH}/lfs: Путь содержимого LFS по умолчанию. (если он находится в локальном хранилище.) УСТАРЕВШЕЕ использование настроек в [lfs]

LFS_JWT_SECRET: пусто: секрет аутентификации LFS, измените эту уникальную строку. Вы можете сгенерировать его с помощью подкоманды Gitea. Командная строка Ref

LFS_JWT_SECRET_URI: пусто: Вместо определения LFS_JWT_SECRET в конфигурации, этот параметр конфигурации может быть использован для предоставления Gitea пути к файлу, содержащему секрет (пример значения:file:/etc/gitea/lfs_jwt_secret)

LFS_HTTP_AUTH_EXPIRY: 24 часа: срок действия аутентификации LFS по времени. Продолжительность, наживания, занимают больше времени, чем это, могут не удается.

LFS_MAX_FILE_SIZE: 0: Максимально допустимый размер файла LFS в байтах (установлено в 0 без ограничений).

LFS_LOCKS_PAGING_NUM: 50: Максимальное количество замков LFS, возвращенных на страницу.

LFS_MAX_BATCH_SIZE: 0: Максимальное количество указателей LFS, которые клиент может запросить в пакетном api LFS. Ноль - это поведение по умолчанию и допускает пакет любого размера.

REDIRECT_OTHER_PORT: false: If true and PROTOCOL is https, allows redirecting http requests on PORT_TO_REDIRECT to the https port Gitea listens on.

REDIRECTOR_USE_PROXY_PROTOCOL: {USE_PROXY_PROTOCOL}: ожидайте заголовок протокола PROXY при подключениях к перенаправлению https.

PORT_TO_REDIRECT: 80: Port for the http redirection service to listen on. Used when REDIRECT_OTHER_PORT is true.

SSL_MIN_VERSION: TLSv1.2: Установите минимальную версию поддержки ssl.

SSL_MAX_VERSION: пусто: Установите максимальную версию поддержки ssl.

SSL_CURVE_PREFERENCES: X25519,P256: Установите предпочтительные кривые,

SSL_CIPHER_SUITES:ecdhe_ecdsa_with_aes_256_gcm_sha384,ecdhe_rsa_with_aes_256_gcm_sha384,ecdhe_ecdsa_with_aes_128_gcm_sha256,ecdhe_rsa_with_aes_128_gcm_sha256,ecdhe_ecdsa_with_chacha20_poly1305,ecdhe_rsa_with_chacha20_poly1305: Установите предпочтительные наборы шифров.

Если для пакетов AES нет аппаратной поддержки, по умолчанию пакеты ChaCha будут предпочтительнее пакетов AES.
поддерживаемые пакеты по состоянию на Go 1.18:
Наборы шифров TLS 1.0 - 1.2
«rsa_with_rc4_128_sha»
"rsa_with_3des_ede_cbc_sha"
"rsa_with_aes_128_cbc_sha"
"rsa_with_aes_256_cbc_sha"
"rsa_with_aes_128_cbc_sha256"
"rsa_with_aes_128_gcm_sha256"
"rsa_with_aes_256_gcm_sha384"
"ecdhe_ecdsa_with_rc4_128_sha"
"ecdhe_ecdsa_with_aes_128_cbc_sha"
"ecdhe_ecdsa_with_aes_256_cbc_sha"
"ecdhe_rsa_with_rc4_128_sha"
"ecdhe_rsa_with_3des_ede_cbc_sha"
"ecdhe_rsa_with_aes_128_cbc_sha"
"ecdhe_rsa_with_aes_256_cbc_sha"
"ecdhe_ecdsa_with_aes_128_cbc_sha256"
"ecdhe_rsa_with_aes_128_cbc_sha256"
"ecdhe_rsa_with_aes_128_gcm_sha256"
"ecdhe_ecdsa_with_aes_128_gcm_sha256"
"ecdhe_rsa_with_aes_256_gcm_sha384"
"ecdhe_ecdsa_with_aes_256_gcm_sha384"
"ecdhe_rsa_with_chacha20_poly1305_sha256"
"ecdhe_ecdsa_with_chacha20_poly1305_sha256"
Наборы шифров TLS 1.3
"aes_128_gcm_sha256"
«aes_256_gcm_sha384»
"chacha20_poly1305_sha256"
Псевдонимные имена
"ecdhe_rsa_with_chacha20_poly1305" - это псевдоним "ecdhe_rsa_with_chacha20_poly1305_sha256"
"ecdhe_ecdsa_with_chacha20_poly1305" - это псевдоним для "ecdhe_ecdsa_with_chacha20_poly1305_sha256"
ENABLE_ACME: false: Flag to enable automatic certificate management via an ACME capable Certificate Authority (CA) server (default: Lets Encrypt). If enabled, CERT_FILE and KEY_FILE are ignored, and the CA must resolve DOMAIN to this gitea server. Ensure that DNS records are set and either port 80 or port 443 are accessible by the CA server (the public internet by default), and redirected to the appropriate ports PORT_TO_REDIRECT or HTTP_PORT respectively.

ACME_URL: пусто: URL-адрес каталога ACME CA, например, для самостоятельно размещенного сервера CA smallstep, он может выглядеть как https://ca.example.com/acme/acme/directory. Если оставить пустым, по умолчанию используется производственный CA Let's Encerypt (проверьте также LETSENCRYPT_ACCEPTTOS).

ACME_ACCEPTTOS: false: Это явная проверка того, что вы принимаете условия обслуживания поставщика ACME. Условия обслуживания Lets Encrypt по умолчанию.

ACME_DIRECTORY: https: Каталог, который менеджер сертификатов будет использовать для кэширования такой информации, как сертификаты и закрытые ключи.

ACME_EMAIL: пусто: Адрес электронной почты, используемый для регистрации ACME. Обычно это уведомление о проблемах с выданными сертификатами.

ACME_CA_ROOT: пусто: Корневой сертификат ЦС. Если оставить пустым, то по умолчанию используется цепочка доверия системы.

ALLOW_GRACEFUL_RESTARTS: true: Выполните изящный перезапуск на SIGHUP

GRACEFUL_HAMMER_TIME: 60s: После перезапуска родительский процесс перестанет принимать новые соединения и позволит завершить запросы перед остановкой. Отключение будет принудительно, если это займет больше времени, чем это время.

STARTUP_TIMEOUT: 0: Выключает сервер, если запуск занимает больше времени, чем указано. В настройках Windows это отправляет ожидание на хост SVC, чтобы сообщить, что запуск хоста SVC может занять некоторое время. Обратите внимание, что запуск определяется открытием слушателей - HTTP/HTTPS/SSH. Индексатеры могут занять больше времени, чтобы начать, и они могут иметь свои собственные тайм-ауты.
