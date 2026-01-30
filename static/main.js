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
    "This website is very mobile compatible,,,! besidesthatweirdresizethingicantwrapmheadaround",
    "\"AI will take your job\" yeah well can AI type this? Taumatawhakatangihangakoauauotamateaturipokakapikimaungahoronukupokaiwhenuakitanatahu",
    "There is a typo in the last splash. I win"
];
const splashes_count = splashes.length;
var current_splash = 0;

var showing_full = true;
var showing_sidenav = false;

var timer = 0;
var timer_id = null;
var title_req_id = 0;

function onload() {
    document.body.onresize();
    load_content_page("home", true);
    setInterval(change_footnote, 30_000);
}

function sleep(ms) {
    return new Promise((resolve) => setTimeout(resolve, ms));
}
// 1070px min
function start_timer() {
    stop_timer();

    timer_id = setInterval(() => {
        for (let i = 0; i < title_bar.children.length; i++) {
            title_bar.children[i].style.translate =
                "0 " + (Math.sin(timer + i / 2) * 15 + "px");
        }
        timer += 0.05;
    }, 20);
}

function stop_timer() {
    if (timer_id) {
        clearInterval(timer_id);
        timer_id = null;
    }
}

async function set_title(title) {
    title_req_id++;
    var title_id = title_req_id;

    while (title_bar.children.length > 0) {
        if (title_req_id != title_id) {
            return;
        }
        title_bar.children[0].remove();

        await sleep(50);
    }

    stop_timer();
    var letter = document.createElement("span");

    if (title_req_id != title_id) {
        return;
    }
    title_bar.appendChild(letter);

    for (let i = 0; i < 2; i++) {
        letter.innerText = "|";
        await sleep(350);
        letter.innerText = "";
        await sleep(350);
    }

    if (title_req_id != title_id) {
        return;
    }
    letter.remove();

    start_timer();
    for (let i = 0; i < title.length; i++) {
        await sleep(50);
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
    var info_req = await fetch("blog/" + page + "/");
    var page_req = await fetch("blog/" + page + "/page/");
    var page = await page_req.text();

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
    content.innerHTML = page;
    content.style.translate = "0 0";
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

    set_superspace(size < 1200);

    showing_sidenav = false;

    if (showing_full) {
        document.body.style.translate = "0 0";
        title_bar.style.cursor = "";
        document.body.classList = ["full"];
    } else {
        document.body.style.translate = "-360px 0";
        title_bar.style.cursor = "pointer";
        document.body.classList = ["stripped"];
    }
}

function set_superspace(enabled) {
    if (enabled) {
        more_top.style.translate = "0 -180px";
        document.body.style.setProperty("--title-font-size", "48px");
        document.body.style.setProperty("--content-font-size", "20px");
        document.body.style.setProperty("--content-small-font-size", "18px");
        document.body.style.setProperty("--content-tiny-font-size", "11px");
    } else {
        more_top.style.translate = "0 0";
        document.body.style.setProperty("--title-font-size", "60px");
        document.body.style.setProperty("--content-font-size", "28px");
        document.body.style.setProperty("--content-small-font-size", "23px");
        document.body.style.setProperty("--content-tiny-font-size", "18px");
    }
}

function toggle_sidenav() {
    if (showing_full) {
        return;
    }

    showing_sidenav = !showing_sidenav;
    if (showing_sidenav) {
        document.body.style.translate = "0 0";
    } else {
        document.body.style.translate = "-360px 0";
    }
}
