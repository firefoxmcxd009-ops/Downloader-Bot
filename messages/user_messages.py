def cancel():
    return "✕ បោះបង់"


def welcome_message(full_name: str = "អ្នកប្រើប្រាស់", user_name: str = None, user_id: int = None) -> str:
    import html
    f_name = html.escape(str(full_name))
    
    # បង្កើត Link ឈ្មោះ User ដោយស្វ័យប្រវត្ត បើគ្មានទិន្នន័យទេវានឹងដាក់ "អ្នកប្រើប្រាស់"
    if user_name:
        u_name = html.escape(str(user_name))
        user_link = f'<a href="https://t.me/{u_name}">{f_name}</a>'
    elif user_id:
        user_link = f'<a href="tg://user?id={user_id}">{f_name}</a>'
    else:
        user_link = f'<b>{f_name}</b>'

    return (
        f'សួរស្តី {user_link} មកកាន់ <a href="https://t.me/amertak_downloaderbot">Amertak Downloader</a> ♡\n\n'
        "ផ្ញើតំណភ្ជាប់ (Link) មួយ ឬច្រើនក្នុងសារតែមួយ ហើយខ្ញុំនឹងទាញយកវីដេអូ/រូបភាពតាមដែលអាចធ្វើបាន។\n\n"
        "◆ <b>គេហទំព័រដែលគាំទ្រ៖</b>\n"
        "☘ Instagram\n"
        "☘ TikTok\n"
        "☘ YouTube\n"
        "☘ X (Twitter)\n"
        "☘ SoundCloud\n"
        "☘ Pinterest\n\n"
        "✎ ប្រើប្រាស់ប៊ូតុងខាងក្រោមដើម្បីសាកល្បង Inline mode, កែការកំណត់ (Settings) ឬចែករំលែក Bot។"
    )


def settings():
    return (
        "<b>⚙ ការកំណត់</b>\n"
        "ប្រើប្រាស់ប៊ូតុងខាងក្រោមដើម្បីកំណត់ទម្រង់នៃការផ្ញើឯកសារដែលបានទាញយក。 "
        "ការផ្លាស់ប្តូរទាំងនេះនឹងអនុវត្តចំពោះតែគណនីរបស់អ្នកប៉ុណ្ណោះ។"
    )


def settings_private_only():
    return (
        "🔒 ការកំណត់អាចធ្វើទៅបានតែនៅក្នុងការជជែកផ្ទាល់ខ្លួន (Private Chat) ប៉ុណ្ណោះ។ សូមបើកសារផ្ទាល់ជាមួយ Bot ដើម្បីផ្លាស់ប្តូរ។"
    )


def get_field_text(field: str):
    texts = {
        "captions": (
            "<b>📝 ការពិពណ៌នា (Captions)</b>\n"
            "បង្ហាញ ឬលាក់ការពិពណ៌នារបស់ផុសនៅក្នុងមេឌៀដែលបានទាញយក។ "
            "ប្រភពមួយចំនួនប្រហែលជាមិនមានការពិពណ៌នាឡើយ。"
        ),
        "delete_message": (
            "<b>🗑 លុបសារ</b>\n"
            "លុបតំណភ្ជាប់ (Link) របស់អ្នកដោយស្វ័យប្រវត្តិ បន្ទាប់ពីការទាញយកត្រូវបានដំណើរការជោគជ័យ។"
        ),
        "info_buttons": (
            "<b>ℹ ប៊ូតុងព័ត៌មាន</b>\n"
            "បើក/បិទ ប៊ូតុងព័ត៌មានបន្ថែមនៅក្រោមមេឌៀដែលបានទាញយក។"
        ),
        "url_button": (
            "<b>🔗 ប៊ូតុង URL</b>\n"
            "បង្ហាញ ឬលាក់ប៊ូតុងដែលមានតំណភ្ជាប់ទៅកាន់ផុសដើម។"
        ),
        "audio_button": (
            "<b>🎧 ប៊ូតុង MP3</b>\n"
            "បើក/បិទ ប៊ូតុងទាញយកឯកសារ MP3 នៅពេលមានសំឡេងដែលអាចទាញយកបាន។"
        ),
    }
    return texts.get(field, "<b>⚙ ការកំណត់</b>\nជម្រើសនេះមិនទាន់មានការពិពណ៌នានៅឡើយទេ។")


def captions(user_captions, post_caption, bot_url, *, limit: int = 1024):
    import html

    def _truncate_escaped(value: str, max_len: int) -> str:
        if max_len <= 0:
            return ""
        if len(value) <= max_len:
            return value
        cut = value[:max_len]
        amp = cut.rfind("&")
        semi = cut.rfind(";")
        if amp > semi:
            cut = cut[:amp]
        return cut

    footer = '🚀 <a href="{bot_url}">Amertak Downloader</a>'.format(bot_url=bot_url)

    if user_captions == "on" and post_caption:
        body = html.escape(str(post_caption))
        sep = "\n\n"
        budget = limit - len(sep) - len(footer)
        if budget <= 0:
            return _truncate_escaped(footer, limit)

        if len(body) > budget:
            suffix = "…"
            body = _truncate_escaped(body, max(0, budget - len(suffix))).rstrip() + suffix

        return f"{body}{sep}{footer}"

    return _truncate_escaped(footer, limit)


def downloading_audio_status():
    return "🎧 កំពុងទាញយកសំឡេង..."


def downloading_video_status():
    return "🎬 កំពុងទាញយកវីដេអូ..."


def uploading_status():
    return "◆ កំពុងបង្ហោះឯកសារទៅកាន់ Telegram..."


def timeout_error():
    return "⏰ អស់ពេលស្នើសុំ។ ប្រភពដើមប្រហែលជាកំពុងមានភាពយឺតយ៉ាវ។ សូមព្យាយាមម្តងទៀតនៅពេលក្រោយ។"


def retrying_again_status(next_attempt: int, total_attempts: int):
    return f"⚠ មានកំហុស កំពុងព្យាយាមម្តងទៀត... ({next_attempt}/{total_attempts})"


def dm_start_required():
    return "🔒 ចាំបាច់ត្រូវរៀបចំជាលើកដំបូង៖ សូមបើកឆាតផ្ទាល់ខ្លួន ចុច Start រួចផ្ញើតំណភ្ជាប់មកម្តងទៀត។"


def duplicate_link_processing():
    return "◆ តំណភ្ជាប់នេះកំពុងត្រូវបានដំណើរការហើយ។ សូមរង់ចាំពីរបីវិនាទី។"


def duplicate_link_recently_processed():
    return "◆ តំណភ្ជាប់នេះទើបតែត្រូវបានដំណើរការរួចរាល់។ ប្រសិនបើអ្នកនៅតែត្រូវការវា សូមព្យាយាមម្តងទៀតក្នុងពេលបន្តិចទៀត។"


def settings_admin_only():
    return "⚠ មានតែអ្នកគ្រប់គ្រងក្រុម (Group Admins) ប៉ុណ្ណោះដែលអាចប្រើ /settings នៅក្នុងក្រុមបាន។"


def invalid_settings_option():
    return "⚠ ជម្រើសការកំណត់មិនត្រឹមត្រូវ។"


def join_group(chat_title: str) -> str:
    return (
        "សូមអរគុណសម្រាប់ការបន្ថែមខ្ញុំទៅក្នុងក្រុម <b>{chat_title}</b> ♡\n"
        "សូមផ្តល់ <b>សិទ្ធិជាអ្នកគ្រប់គ្រង (Admin Rights)</b> ដល់ខ្ញុំ ដើម្បីអាចដំណើរការមុខងារបានពេញលេញ 🔓"
    ).format(chat_title=chat_title)


def admin_rights_granted(chat_title: str) -> str:
    return (
        "សូមអរគុណសម្រាប់ការផ្តល់សិទ្ធិជាអ្នកគ្រប់គ្រងនៅក្នុងក្រុម <b>{chat_title}</b> ☘\n"
        "✎ ខ្ញុំនឹងរក្សាការទាញយកឲ្យដំណើរការទៅដោយរលូន។"
    ).format(chat_title=chat_title)


def something_went_wrong():
    return (
        "⚠ មិនអាចដំណើរការតំណភ្ជាប់នេះបានទេនៅពេលនេះ។\n"
        "វាអាចជាគណនីឯកជន (Private), ត្រូវបានលុប, ជាប់កម្រិតតំបន់ ឬត្រូវបានរារាំងជាបណ្តោះអាសន្នពីប្រភពដើម។ "
        "សូមព្យាយាមម្តងទៀតនៅពេលក្រោយ。"
    )


def video_too_large():
    return "⚠ វីដេអូនេះមានទំហំធំពេកសម្រាប់ Telegram។ សូមសាកល្បងវីដេអូដែលមានរយៈពេលខ្លីជាងនេះ ឬជ្រើសរើសជម្រើស MP3/សំឡេង បើមាន។"


def audio_too_large():
    return "⚠ ឯកសារសំឡេងនេះមានទំហំធំពេកសម្រាប់ Telegram។ សូមសាកល្បងបទចម្រៀងដែលខ្លីជាងនេះ ឬប្រើប្រាស់តំណភ្ជាប់ផ្សេងទៀត។"


def nothing_found():
    return "⚠ រកមិនឃើញមេឌៀឡើយ។ សូមពិនិត្យមើលថាតើតំណភ្ជាប់នោះជាសាធារណៈ (Public) មិនទាន់ហួសកំណត់ និងនាំទៅកាន់ផុស ឬវីដេអូដោយផ្ទាល់។"


def keyboard_removed():
    return "✕ បានលុបផ្ទាំងចុចបញ្ជា (Reply Keyboard) ចេញរួចរាល់។"


def tiktok_live_not_supported():
    return "⚠ មិនទាន់គាំទ្រការទាញយក TikTok LIVE នៅឡើយទេ។ សូមផ្ញើតំណភ្ជាប់នៃផុស TikTok ធម្មតា។"


def delete_permission_warning():
    return "⚠ ការលុបស្វ័យប្រវត្តិបានបរាជ័យ៖ ខ្វះសិទ្ធិក្នុងការលុបសារនៅក្នុងក្រុមនេះ។ សូមផ្តល់សិទ្ធិលុបសារ ឬបិទមុខងារលុបស្វ័យប្រវត្តនៅក្នុងការកំណត់ (Settings)។"


def stats_temporarily_unavailable():
    return "⚠ មិនអាចបង្កើតទិន្នន័យស្ថិតិបានទេនៅពេលនេះ។ សូមព្យាយាមម្តងទៀតនៅពេលក្រោយ។"


def no_queue_metrics_yet():
    return "◆ មិនទាន់មានទិន្នន័យជួររង់ចាំ (Queue) នៅឡើយទេ។"


def open_bot_for_audio():
    return "🎧 សូមបើក Bot នៅក្នុងឆាតផ្ទាល់ខ្លួនដើម្បីទាញយកឯកសារសំឡេង។"


def audio_fetch_failed():
    return "⚠ ការទាញយកព័ត៌មានសំឡេងបានបរាជ័យ។ សូមព្យាយាមម្តងទៀតនៅពេលក្រោយ។"


def audio_download_failed():
    return "⚠ ការទាញយកឯកសារសំឡេងបានបរាជ័យ។ សូមព្យាយាមម្តងទៀតនៅពេលក្រោយ។"


def inline_album_link_invalid():
    return "⚠ តំណភ្ជាប់អាល់ប៊ុមនេះបានហួសកំណត់ ឬមិនត្រឹមត្រូវ។"


def inline_photo_title(service_name: str):
    return f"រូបភាព {service_name}"


def inline_photo_description():
    return "រូបភាពទោល"


def inline_album_title(service_name: str):
    return f"អាល់ប៊ុម {service_name}"


def inline_album_description():
    return "បើកអាល់ប៊ុមពេញនៅក្នុង Bot"


def inline_open_full_album_button():
    return "◆ បើកអាល់ប៊ុមពេញ"


def inline_photos_title(service_name: str):
    return f"រូបភាព {service_name}"


def inline_photos_not_supported(service_name: str):
    return f"រូបភាពរបស់ {service_name} មិនគាំទ្រនៅលើ Inline mode ឡើយ។"


def inline_send_video_button():
    return "◆ ផ្ញើវីដេអូជា Inline"


def inline_send_video_prompt(service_name: str):
    return f"វីដេអូរបស់ {service_name} កំពុងត្រូវបានរៀបចំ...\nប្រសិនបើវាមិនចាប់ផ្តើមដោយស្វ័យប្រវត្តិទេ សូមចុចប៊ូតុងខាងក្រោម។"


def inline_send_audio_prompt(service_name: str):
    return f"សំឡេងរបស់ {service_name} កំពុងត្រូវបានរៀបចំ...\nប្រសិនបើវាមិនចាប់ផ្តើមដោយស្វ័យប្រវត្តិទេ សូមចុចប៊ូតុងខាងក្រោម។"


def inline_video_already_processing():
    return "◆ វីដេអូ Inline នេះកំពុងស្ថិតក្នុងរៀបចំរួចរាល់ហើយ។"


def inline_video_already_sent():
    return "◆ វីដេអូ Inline នេះត្រូវបានផ្ញើរួចហើយ។"


def supported_sites_message():
    return (
        "<b>◆ គេហទំព័រដែលគាំទ្រ</b>\n\n"
        "☘ Instagram: ផុស, Reels, និងអាល់ប៊ុម\n"
        "☘ TikTok: វីដេអូ, ផុសរូបភាព, និងកម្រងព័ត៌មាន (Profiles)\n"
        "☘ YouTube: វីដេអូ និងតំណភ្ជាប់ YouTube Music\n"
        "☘ X / Twitter: រាល់ផុសទាំងអស់\n"
        "☘ SoundCloud: រាល់បទចម្រៀង\n"
        "☘ Pinterest: រាល់ការរក្សាទុក (Pins)\n\n"
        "អ្នកអាចផ្ញើតំណភ្ជាប់ដែលគាំទ្រជាច្រើនក្នុងសារតែមួយ។ Amertak Downloader នឹងដំណើរការពួកវាម្តងមួយៗ។"
    )


def batch_links_started(processed_total: int, detected_total: int | None = None):
    if detected_total is not None and detected_total > processed_total:
        return (
            f"◆ រកឃើញតំណភ្ជាប់ដែលគាំទ្រចំនួន {detected_total}។ "
            f"ខ្ញុំនឹងដំណើរការ {processed_total} ដំបូងម្តងមួយៗ ដើម្បីកុំឱ្យការជជែកមានភាពរញ៉េរញ៉ៃ។"
        )
    return f"◆ រកឃើញតំណភ្ជាប់ដែលគាំទ្រចំនួន {processed_total}។ ខ្ញុំនឹងដំណើរការពួកវាម្តងមួយៗ ដើម្បីកុំឱ្យការជជែកមានភាពរញ៉េរញ៉ៃ។"


def batch_link_progress(current: int, total: int, service_name: str):
    return f"✎ កំពុងដំណើរការតំណភ្ជាប់ទី {current}/{total}: {service_name}..."


def batch_links_finished(total: int):
    return f"✓ បានបញ្ចប់ការដំណើរការជាក្រុមសម្រាប់តំណភ្ជាប់ចំនួន {total} រួចរាល់។"
