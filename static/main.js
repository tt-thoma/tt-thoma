// tt_thoma
const splashes = [
    "Website built from scratch by tt_thoma!",
    "Hey google, center that div",
    "Yes, I, when the... when I you know, the I... nevermind.",
    "This text is in fact, not yellow.",
    "Also try Terraria!",
    "Is someone even looking at these?",
    "That cake is 100% real",
    "Hey chatgpt, center that div",
    "I fix the website for the mobile user s!!",
    "\"AI will take your job\" yeah well can AI type this? Taumatawhakatangihangakoauauotamateaturipokakapikimaungahoronukupokaiwhenuakitanatahu",
    "There is a typo in the last splash. I win"
];

const splashes_count = splashes.length;
var current_splash = 0;

var showing_full = true;
var showing_sidenav = false;

var animation_timer = 0;
var animation_timer_id;
var title_req_id = 0;

var loader_id;
var url_params;
var current_page;

// Try loading the page earlier than what body.onload allows
loader_id = setInterval(() => {
    try { onload(); clearInterval(loader_id); }
    catch {}
}, 500)

function onload() {
    document.body.onresize();
    set_title("Loading...", true);

    parse_url();
    if (url_params.has("page")) {
        load_content_page(url_params.get("page"));
    } else {
        load_content_page("welcome");
    }

    setInterval(change_footnote, 30_000);
}

function parse_url() {
    url_params = new URLSearchParams(window.location.href.split("?")[1]);
}

function sleep(ms) {
    return new Promise((resolve) => setTimeout(resolve, ms));
}

function start_animation_timer() {
    stop_animation_timer();

    animation_timer_id = setInterval(() => {
        for (let i = 0; i < title_bar.children.length; i++) {
            title_bar.children[i].style.translate =
                "0 " + (Math.sin(animation_timer + i / 2) * 15 + "px");
        }
        animation_timer += 0.05;
    }, 20);
}

function stop_animation_timer() {
    if (animation_timer_id) {
        clearInterval(animation_timer_id);
        animation_timer_id = null;
    }
}

async function set_title(title, immediate) {
    title_req_id++;
    var title_id = title_req_id;

    while (title_bar.children.length > 0) {
        if (title_req_id != title_id) {
            return;
        }
        title_bar.children[0].remove();
        
        if (!immediate) { await sleep(50); }
    }

    stop_animation_timer();
    var letter = document.createElement("span");

    if (title_req_id != title_id) {
        return;
    }
    title_bar.appendChild(letter);

    if (!immediate) {
        for (let i = 0; i < 2; i++) {
            letter.innerText = "|";
            await sleep(350);
            letter.innerText = "";
            await sleep(350);
        }
    }

    if (title_req_id != title_id) {
        return;
    }
    letter.remove();

    start_animation_timer();
    for (let i = 0; i < title.length; i++) {
        if (!immediate) { await sleep(50); }

        var letter = document.createElement("span");
        if (!title.charAt(i).trim()) {
            letter.style.width = "30px";
        }
        letter.innerText = title.charAt(i);

        if (title_req_id != title_id) {
            return;
        }
        title_bar.appendChild(letter);
    }

    if (title_req_id != title_id) {
        return;
    }
    title_setting = false;
}

async function load_content_page(page, immediate) {
    if (current_page == page) {
        return;
    }

    var info_req = await fetch("blog/" + page + "/");
    var page_req = await fetch("blog/" + page + "/page/");
    var page_text = await page_req.text();

    if (info_req.ok) {
        var page_info = await info_req.json();
        set_title(">> " + page_info["name"]);
    } else {
        set_title(">>!! " + info_req.status + " (" + info_req.statusText + ")");
    }
    // We replace it even if it error out
    content.style.translate = "0 120vh";
    if (!immediate) {
        await sleep(1100);
    }
    content.innerHTML = page_text;
    content.style.translate = "0 0";

    current_page = page;
}

async function set_footnote(note) {
    footnote.style.translate = "0 50px";
    await sleep(1100);
    footnote.innerText = note;
    footnote.style.translate = "0 0";
}

function change_footnote() {
    current_splash++;
    current_splash %= splashes_count;
    set_footnote(splashes[current_splash]);
}

function set_width_adapt() {
    var size = document.body.clientWidth;

    if (showing_full) {
        showing_full = (size > 1400);
    } else {
        showing_full = (size > 1700);
    }

    if (showing_full) {
        showing_sidenav = false;
        wrapper.style.translate = "0 0";
        wrapper.classList = "full";
    } else {
        update_sidenav();
        wrapper.classList = "stripped";
        set_superspace(size < 930);
    }
}

function set_superspace(enabled) {
    if (enabled) {
        wrapper.classList += " superspace";
    }
}

function update_sidenav() {
    if (showing_full) {
        return;
    }

    if (showing_sidenav) {
        wrapper.style.translate = "0 0";
    } else {
        wrapper.style.translate = "-300px 0";
    }
}

function toggle_sidenav() {
    if (showing_full) {
        return;
    }

    showing_sidenav = !showing_sidenav;
    update_sidenav();
}
