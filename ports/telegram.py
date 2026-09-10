"""Telegram Desktop: a .tdesktop-theme per flavor, covering every key of the desktop palette."""

import struct
import zlib

import palette as p
from ports._lib import HEADER, Out, ink, tints, ui_colors, zip_bytes

# Every key of desktop-app/lib_ui ui/colors.palette, in file order.
#   key        a literal color upstream: must be mapped in colors() below
#   key=ref    a copy of another key upstream: follows it unless mapped
#   key|ref    a literal with a fallback upstream: follows the fallback unless mapped
SPEC = """
windowBg windowFg windowBgOver windowBgRipple windowFgOver=windowFg windowSubTextFg
windowSubTextFgOver windowBoldFg windowBoldFgOver windowBgActive windowFgActive windowActiveTextFg
windowShadowFg windowShadowFgFallback shadowFg slideFadeOutBg slideFadeOutShadowFg=windowShadowFg
imageBg imageBgTransparent activeButtonBg=windowBgActive activeButtonBgOver activeButtonBgRipple
activeButtonFg=windowFgActive activeButtonFgOver=activeButtonFg activeButtonSecondaryFg
activeButtonSecondaryFgOver=activeButtonSecondaryFg activeLineFg activeLineFgError
lightButtonBg=windowBg lightButtonBgOver lightButtonBgRipple lightButtonFg=windowActiveTextFg
lightButtonFgOver=lightButtonFg attentionButtonFg attentionButtonFgOver attentionButtonBgOver
attentionButtonBgRipple menuBg=windowBg menuBgOver=windowBgOver menuBgRipple=windowBgRipple
menuIconFg menuIconFgOver menuSubmenuArrowFg menuFgDisabled menuSeparatorFg scrollBarBg
scrollBarBgOver scrollBg scrollBgOver smallCloseIconFg smallCloseIconFgOver radialFg=windowFgActive
radialBg placeholderFg=windowSubTextFg placeholderFgActive inputBorderFg filterInputBorderFg
filterInputActiveBg=windowBg filterInputInactiveBg=windowBgOver checkboxFg botKbBg=menuBgOver
botKbDownBg=menuBgRipple botKbColor=windowBoldFgOver botKbPrimaryBg botKbDangerBg botKbSuccessBg
botKbInlinePrimaryBg botKbInlineDangerBg botKbInlineSuccessBg sliderBgInactive
sliderBgActive=windowBgActive tooltipBg tooltipFg tooltipBorderFg titleShadow titleBg=windowBgOver
titleBgActive=titleBg titleButtonBg=titleBg titleButtonFg titleButtonBgOver titleButtonFgOver
titleButtonBgActive=titleButtonBg titleButtonFgActive=titleButtonFg
titleButtonBgActiveOver=titleButtonBgOver titleButtonFgActiveOver=titleButtonFgOver
titleButtonCloseBg=titleButtonBg titleButtonCloseFg=titleButtonFg titleButtonCloseBgOver
titleButtonCloseFgOver=windowFgActive titleButtonCloseBgActive=titleButtonCloseBg
titleButtonCloseFgActive=titleButtonCloseFg titleButtonCloseBgActiveOver=titleButtonCloseBgOver
titleButtonCloseFgActiveOver=titleButtonCloseFgOver titleFg titleFgActive trayCounterBg
trayCounterBgMute trayCounterFg trayCounterBgMacInvert trayCounterFgMacInvert layerBg
cancelIconFg=menuIconFg cancelIconFgOver=menuIconFgOver boxBg=windowBg boxTextFg=windowFg
boxTextFgGood boxTextFgError boxTitleFg boxSearchBg=boxBg boxTitleAdditionalFg
boxTitleCloseFg=cancelIconFg boxTitleCloseFgOver=cancelIconFgOver boxDividerBg=windowBgOver
boxDividerFg=windowShadowFg paymentsTipActive membersAboutLimitFg=windowSubTextFgOver
contactsBg=windowBg contactsBgOver=windowBgOver contactsNameFg=boxTextFg
contactsStatusFg=windowSubTextFg contactsStatusFgOver=windowSubTextFgOver
contactsStatusFgOnline=windowActiveTextFg photoCropFadeBg=layerBg photoCropPointFg
callArrowFg|boxTextFgGood callArrowMissedFg|boxTextFgError introBg=windowBg
introTitleFg=windowBoldFg introDescriptionFg=windowSubTextFg introCoverTopBg introCoverBottomBg
introCoverIconsFg introCoverPlaneTrace introCoverPlaneInner introCoverPlaneOuter introCoverPlaneTop
dialogsMenuIconFg=menuIconFg dialogsMenuIconFgOver=menuIconFgOver dialogsBg=windowBg
dialogsNameFg=windowBoldFg dialogsChatIconFg=dialogsNameFg dialogsDateFg=windowSubTextFg
dialogsTextFg=windowSubTextFg dialogsTextFgService=windowActiveTextFg dialogsDraftFg
dialogsVerifiedIconBg=windowBgActive dialogsVerifiedIconFg=windowFgActive dialogsSendingIconFg
dialogsSentIconFg dialogsUnreadBg=windowBgActive dialogsUnreadBgMuted dialogsUnreadFg=windowFgActive
dialogsArchiveFg|dialogsNameFg dialogsOnlineBadgeFg|dialogsUnreadBg dialogsScamFg=dialogsDraftFg
dialogsBgOver=windowBgOver dialogsNameFgOver=windowBoldFgOver
dialogsChatIconFgOver=dialogsNameFgOver dialogsDateFgOver=windowSubTextFgOver
dialogsTextFgOver=windowSubTextFgOver dialogsTextFgServiceOver=dialogsTextFgService
dialogsDraftFgOver=dialogsDraftFg dialogsVerifiedIconBgOver=dialogsVerifiedIconBg
dialogsVerifiedIconFgOver=dialogsVerifiedIconFg dialogsSendingIconFgOver=dialogsSendingIconFg
dialogsSentIconFgOver dialogsUnreadBgOver=dialogsUnreadBg
dialogsUnreadBgMutedOver=dialogsUnreadBgMuted dialogsUnreadFgOver=dialogsUnreadFg
dialogsArchiveFgOver|dialogsNameFgOver dialogsScamFgOver=dialogsDraftFgOver dialogsBgActive
dialogsNameFgActive=windowFgActive dialogsChatIconFgActive=dialogsNameFgActive
dialogsDateFgActive=windowFgActive dialogsTextFgActive=windowFgActive
dialogsTextFgServiceActive=dialogsTextFgActive dialogsDraftFgActive
dialogsVerifiedIconBgActive=dialogsTextFgActive dialogsVerifiedIconFgActive=dialogsBgActive
dialogsSendingIconFgActive dialogsSentIconFgActive=dialogsTextFgActive
dialogsUnreadBgActive=dialogsTextFgActive dialogsUnreadBgMutedActive=dialogsDraftFgActive
dialogsUnreadFgActive=dialogsBgActive dialogsOnlineBadgeFgActive
dialogsScamFgActive=dialogsDraftFgActive dialogsRippleBg=windowBgRipple
dialogsRippleBgActive=activeButtonBgRipple searchedBarBg=windowBgOver
searchedBarFg=windowSubTextFgOver searchedTextMatchBg searchedTextMatchFg searchedTextCurrentMatchBg
searchedTextCurrentMatchFg topBarBg=windowBg emojiPanBg=windowBg emojiPanCategories|windowBg
emojiPanHeaderFg=windowSubTextFg emojiPanHeaderBg|emojiPanBg emojiIconFg
emojiSubIconFgActive|windowBoldFg stickerPanDeleteBg stickerPanDeleteFg=windowFgActive
stickerPreviewBg stickerPanPremium1 stickerPanPremium2 historyTextInFg=windowFg
historyTextInFgSelected=historyTextInFg historyTextOutFg=windowFg
historyTextOutFgSelected=historyTextOutFg historyLinkInFg=windowActiveTextFg
historyLinkInFgSelected=historyLinkInFg historyLinkOutFg=windowActiveTextFg
historyLinkOutFgSelected=historyLinkOutFg historyFileNameInFg=historyTextInFg
historyFileNameInFgSelected=historyFileNameInFg historyFileNameOutFg=historyTextOutFg
historyFileNameOutFgSelected=historyFileNameOutFg historyOutIconFg historyOutIconFgSelected
historyIconFgInverted=windowFgActive historySendingOutIconFg historySendingInIconFg
historySendingInvertedIconFg historyCallArrowInFg historyCallArrowInFgSelected
historyCallArrowMissedInFg=callArrowMissedFg historyCallArrowMissedInFgSelected=callArrowMissedFg
historyCallArrowOutFg=historyCallArrowInFg
historyCallArrowOutFgSelected=historyCallArrowInFgSelected historyUnreadBarBg
historyUnreadBarBorder=shadowFg historyUnreadBarFg historyForwardChooseBg
historyForwardChooseFg=windowFgActive historyPeer1NameFg
historyPeer1NameFgSelected=historyPeer1NameFg historyPeer1UserpicBg historyPeer2NameFg
historyPeer2NameFgSelected=historyPeer2NameFg historyPeer2UserpicBg historyPeer3NameFg
historyPeer3NameFgSelected=historyPeer3NameFg historyPeer3UserpicBg
historyPeer4NameFg=windowActiveTextFg historyPeer4NameFgSelected=historyPeer4NameFg
historyPeer4UserpicBg historyPeer5NameFg historyPeer5NameFgSelected=historyPeer5NameFg
historyPeer5UserpicBg historyPeer6NameFg historyPeer6NameFgSelected=historyPeer6NameFg
historyPeer6UserpicBg historyPeer7NameFg historyPeer7NameFgSelected=historyPeer7NameFg
historyPeer7UserpicBg historyPeer8NameFg historyPeer8NameFgSelected=historyPeer8NameFg
historyPeer8UserpicBg historyPeerUserpicFg=windowFgActive
historyPeerSavedMessagesBg=historyPeer4UserpicBg historyPeerArchiveUserpicBg=dialogsUnreadBgMuted
historyPeer1UserpicBg2|historyPeer1UserpicBg historyPeer2UserpicBg2|historyPeer2UserpicBg
historyPeer3UserpicBg2|historyPeer3UserpicBg historyPeer4UserpicBg2|historyPeer4UserpicBg
historyPeer5UserpicBg2|historyPeer5UserpicBg historyPeer6UserpicBg2|historyPeer6UserpicBg
historyPeer7UserpicBg2|historyPeer7UserpicBg historyPeer8UserpicBg2|historyPeer8UserpicBg
historyPeerSavedMessagesBg2=historyPeer4UserpicBg2 settingsIconBg1 settingsIconBg2 settingsIconBg3
settingsIconBg4 settingsIconBg5 settingsIconBg6 settingsIconBg8 settingsIconBgArchive settingsIconFg
historyScrollBarBg historyScrollBarBgOver historyScrollBg historyScrollBgOver msgInBg=windowBg
msgInBgSelected msgOutBg msgOutBgSelected msgSelectOverlay msgStickerOverlay
msgInServiceFg=windowActiveTextFg msgInServiceFgSelected=windowActiveTextFg msgOutServiceFg
msgOutServiceFgSelected msgInShadow msgInShadowSelected msgOutShadow msgOutShadowSelected
msgInDateFg msgInDateFgSelected msgOutDateFg msgOutDateFgSelected msgServiceFg=windowFgActive
msgServiceBg msgServiceBgSelected msgInReplyBarColor=activeLineFg msgInReplyBarSelColor=activeLineFg
msgOutReplyBarColor msgOutReplyBarSelColor=historyOutIconFgSelected msgImgReplyBarColor=msgServiceFg
msgInMonoFg msgOutMonoFg msgInMonoFgSelected=msgInMonoFg msgOutMonoFgSelected=msgOutMonoFg
msgDateImgFg=msgServiceFg msgDateImgBg msgDateImgBgOver msgDateImgBgSelected
msgFileThumbLinkInFg=lightButtonFg msgFileThumbLinkInFgSelected=lightButtonFgOver
msgFileThumbLinkOutFg msgFileThumbLinkOutFgSelected msgFileInBg=windowBgActive msgFileInBgOver
msgFileInBgSelected msgFileOutBg msgFileOutBgSelected msgFile1Bg msgFile1BgDark msgFile1BgOver
msgFile1BgSelected msgFile2Bg msgFile2BgDark msgFile2BgOver msgFile2BgSelected msgFile3Bg
msgFile3BgDark msgFile3BgOver msgFile3BgSelected msgFile4Bg msgFile4BgDark msgFile4BgOver
msgFile4BgSelected historyFileInIconFg=msgInBg historyFileInIconFgSelected=msgInBgSelected
historyFileInRadialFg=historyFileInIconFg historyFileInRadialFgSelected=historyFileInIconFgSelected
historyFileOutIconFg=msgOutBg historyFileOutIconFgSelected=msgOutBgSelected
historyFileOutRadialFg=historyFileOutIconFg
historyFileOutRadialFgSelected=historyFileOutIconFgSelected historyFileThumbIconFg=msgInBg
historyFileThumbIconFgSelected=msgInBgSelected historyFileThumbRadialFg=historyFileThumbIconFg
historyFileThumbRadialFgSelected=historyFileThumbIconFgSelected
historyVideoMessageProgressFg=historyFileThumbIconFg msgWaveformInActive=windowBgActive
msgWaveformInActiveSelected msgWaveformInInactive msgWaveformInInactiveSelected msgWaveformOutActive
msgWaveformOutActiveSelected msgWaveformOutInactive msgWaveformOutInactiveSelected msgBotKbOverBgAdd
msgBotKbIconFg=msgServiceFg msgBotKbRippleBg mediaInFg=msgInDateFg
mediaInFgSelected=msgInDateFgSelected mediaOutFg=msgOutDateFg
mediaOutFgSelected=msgOutDateFgSelected youtubePlayIconBg youtubePlayIconFg=windowFgActive
videoPlayIconBg videoPlayIconFg toastBg toastFg historyToDownBg=windowBg
historyToDownBgOver=windowBgOver historyToDownBgRipple=windowBgRipple historyToDownFg=menuIconFg
historyToDownFgOver=menuIconFgOver historyToDownShadow historyComposeAreaBg=msgInBg
historyComposeAreaFg=historyTextInFg historyComposeAreaFgService=msgInDateFg
historyComposeIconFg=menuIconFg historyComposeIconFgOver=menuIconFgOver
historySendIconFg=windowBgActive historySendIconFgOver=windowBgActive
historyPinnedBg=historyComposeAreaBg historyReplyBg=historyComposeAreaBg
historyReplyIconFg=windowBgActive historyReplyCancelFg=cancelIconFg
historyReplyCancelFgOver=cancelIconFgOver historyComposeButtonBg=historyComposeAreaBg
historyComposeButtonBgOver=windowBgOver historyComposeButtonBgRipple=windowBgRipple mapPointDrop
mapPointDot overviewCheckBg overviewCheckBgActive=windowBgActive overviewCheckBorder=windowBg
overviewCheckFgActive=windowBg overviewPhotoSelectOverlay profileStatusFgOver
profileVerifiedCheckBg=windowBgActive profileVerifiedCheckFg=windowFgActive
profileAdminStartFg=windowBgActive notificationsBoxMonitorFg=windowFg
notificationsBoxScreenBg=dialogsBgActive notificationSampleUserpicFg=windowBgActive
notificationSampleCloseFg|windowSubTextFg notificationSampleTextFg|windowSubTextFg
notificationSampleNameFg|windowSubTextFg mainMenuBg=windowBg mainMenuCoverBg=dialogsBgActive
mainMenuCloudFg=activeButtonFg mainMenuCloudBg|activeButtonBgRipple mediaPlayerBg=windowBg
mediaPlayerActiveFg=windowBgActive mediaPlayerInactiveFg=sliderBgInactive mediaPlayerDisabledFg
mediaviewFileBg=windowBg mediaviewFileNameFg=windowFg mediaviewFileSizeFg=windowSubTextFg
mediaviewFileRedCornerFg mediaviewFileYellowCornerFg mediaviewFileGreenCornerFg
mediaviewFileBlueCornerFg mediaviewFileExtFg=activeButtonFg mediaviewMenuBg mediaviewMenuBgOver
mediaviewMenuBgRipple mediaviewMenuFg=windowFgActive mediaviewBg mediaviewVideoBg=imageBg
mediaviewControlBg mediaviewControlFg mediaviewCaptionBg mediaviewCaptionFg=mediaviewControlFg
mediaviewTextLinkFg mediaviewSaveMsgBg=toastBg mediaviewSaveMsgFg=toastFg mediaviewPlaybackActive
mediaviewPlaybackInactive mediaviewPlaybackActiveOver mediaviewPlaybackInactiveOver
mediaviewPlaybackProgressFg mediaviewPlaybackIconFg=mediaviewPlaybackActive
mediaviewPlaybackIconFgOver=mediaviewPlaybackActiveOver mediaviewPlaybackIconRipple
mediaviewPipControlsFg mediaviewPipControlsFgOver mediaviewPipPlaybackActive
mediaviewPipPlaybackInactive mediaviewTransparentBg mediaviewTransparentFg notificationBg=windowBg
callBg callBgOpaque callBgButton callNameFg callStatusFg callIconBg callIconFg callIconBgActive
callIconFgActive callIconActiveRipple callAnswerBg callAnswerRipple callAnswerBgOuter callHangupBg
callHangupRipple callMuteRipple groupCallBg groupCallActiveFg groupCallMembersBg
groupCallMembersBgOver groupCallMembersBgRipple groupCallMembersFg groupCallMemberActiveIcon
groupCallMemberActiveStatus groupCallMemberInactiveIcon groupCallMemberInactiveStatus
groupCallMemberMutedIcon groupCallMemberNotJoinedStatus groupCallIconFg groupCallLive1
groupCallLive2 groupCallMuted1 groupCallMuted2 groupCallForceMutedBar1 groupCallForceMutedBar2
groupCallForceMutedBar3 groupCallForceMuted1 groupCallForceMuted2 groupCallForceMuted3
groupCallMenuBg groupCallMenuBgOver groupCallMenuBgRipple groupCallLeaveBg groupCallLeaveBgRipple
groupCallVideoTextFg groupCallVideoSubTextFg callBarBg=dialogsBgActive
callBarMuteRipple=dialogsRippleBgActive callBarBgMuted|dialogsUnreadBgMuted
callBarFg=dialogsNameFgActive importantTooltipBg=toastBg importantTooltipFg=toastFg
importantTooltipFgLink=mediaviewTextLinkFg outdatedFg outdateSoonBg outdatedBg
spellUnderline|attentionButtonFg walletTitleBg walletTitleBgActive=walletTitleBg
walletTitleButtonBg=walletTitleBg walletTitleButtonFg walletTitleButtonBgOver
walletTitleButtonFgOver walletTitleButtonBgActive=walletTitleButtonBg
walletTitleButtonFgActive=walletTitleButtonFg walletTitleButtonBgActiveOver=walletTitleButtonBgOver
walletTitleButtonFgActiveOver=walletTitleButtonFgOver walletTitleButtonCloseBg=walletTitleButtonBg
walletTitleButtonCloseFg=walletTitleButtonFg walletTitleButtonCloseBgOver=titleButtonCloseBgOver
walletTitleButtonCloseFgOver=titleButtonCloseFgOver
walletTitleButtonCloseBgActive=walletTitleButtonCloseBg
walletTitleButtonCloseFgActive=walletTitleButtonCloseFg
walletTitleButtonCloseBgActiveOver=walletTitleButtonCloseBgOver
walletTitleButtonCloseFgActiveOver=walletTitleButtonCloseFgOver walletTopBg walletBalanceFg
walletSubBalanceFg walletTopLabelFg walletTopIconFg=walletTopLabelFg walletTopIconRipple sideBarBg
sideBarBgActive sideBarBgRipple sideBarTextFg sideBarTextFgActive sideBarIconFg sideBarIconFgActive
sideBarBadgeBg sideBarBadgeBgActive=sideBarBadgeBg sideBarBadgeBgMuted
sideBarBadgeBgMutedActive=sideBarBadgeBg sideBarBadgeFg songCoverOverlayFg
photoEditorItemBaseHandleFg premiumButtonBg1 premiumButtonBg2 premiumButtonBg3 premiumButtonFg
premiumIconBg1 premiumIconBg2 premiumIconBg3 statisticsChartInactive statisticsChartActive
statisticsChartLineBlue statisticsChartLineGreen statisticsChartLineRed statisticsChartLineGolden
statisticsChartLineLightblue statisticsChartLineLightgreen statisticsChartLineOrange
statisticsChartLineIndigo statisticsChartLinePurple statisticsChartLineCyan creditsBg1 creditsBg2
creditsBg3 creditsFg creditsStroke currencyFg rankAdminFg rankOwnerFg rankUserFg=windowSubTextFg
dialogsMentionIconFg|dialogsVerifiedIconBg dialogsReactionIconFg|attentionButtonFg
dialogsPollIconFg|historyPeer5NameFg
"""


KEY_COUNT = len(SPEC.split())

META = {
    "id": "telegram",
    "name": "Telegram",
    "category": "Apps",
    "homepage": "https://desktop.telegram.org",
    "enable": {
        "where": "Telegram Desktop › Settings › Chat Settings",
        "code": "Choose from file › {slug}.tdesktop-theme, then Keep changes\n"
        "(opening the file with Telegram Desktop does the same)",
        "lang": "text",
    },
    "auto": {
        "where": "Telegram Desktop",
        "code": "Telegram keeps one theme for day and one for Night Mode (main menu › Night Mode):\n"
        "with Night Mode off, open subway-seat-enamel.tdesktop-theme;\n"
        "with Night Mode on, open subway-seat.tdesktop-theme (or subway-seat-tunnel);\n"
        "then click Settings › Chat Settings › Auto-night mode until it reads System.",
        "lang": "text",
    },
    "detect": ["/Applications/Telegram Desktop.app", "telegram-desktop"],
    "notes": f"Sets all {KEY_COUNT} keys of the Telegram Desktop palette, with a plain walnut chat background "
    "bundled in. Outgoing bubbles take a soft orange tint; media viewer and calls stay dark in every flavor. "
    "For Telegram Desktop only; the native macOS app doesn't take theme files.",
}

def _a(color, alpha):
    """#RRGGBB + alpha (0..1) → #RRGGBBAA."""
    return p.alpha(color, alpha)


def colors(f):
    """The literal (non-derived) keys, resolved for flavor f."""
    c = f
    dark = f.dark
    night = f if dark else p.WALNUT      # media viewer, calls and wallet stay dark in every flavor
    on = ink(f)                          # text on an accent fill
    bad = c.red_hi if dark else c.red
    shade = c.crust if dark else c.text_hi   # shadow and fade tint
    over_bg = c.crust if dark else c.text_hi  # translucent pills over photos and video
    over_fg = c.text_hi if dark else c.base   # text and icons on those pills
    on_red = c.text_hi if dark else c.base

    def deep(color, t=0.82):
        return f.mix(color, p.WALNUT.crust, t)

    def tint(color, t):
        return f.mix(color, "base", t)

    paper = ui_colors(f)["paper"]  # menus and tooltips are raised onto paper
    t = tints(f)
    out_bg = tint("orange", 0.18 if dark else 0.14)
    out_sel = tint("orange", 0.30 if dark else 0.24)
    peers = [c.red_hi, c.green, c.yellow, c.denim, c.clay, c.orange_hi, c.sage, c.orange]

    m = {
        # basic
        "windowBg": c.base, "windowFg": c.text,
        "windowBgOver": c.surface0, "windowBgRipple": c.surface1,
        "windowSubTextFg": c.overlay2, "windowSubTextFgOver": c.subtext0,
        "windowBoldFg": c.text_hi, "windowBoldFgOver": c.text_hi,
        "windowBgActive": c.orange, "windowFgActive": on, "windowActiveTextFg": c.orange,
        "windowShadowFg": shade, "windowShadowFgFallback": c.crust,
        "shadowFg": _a(shade, 0.22 if dark else 0.10), "slideFadeOutBg": _a(shade, 0.24),
        "imageBg": c.crust, "imageBgTransparent": c.base,
        # buttons, inputs, menus
        "activeButtonBgOver": c.orange_hi, "activeButtonBgRipple": f.mix("orange", on, 0.78),
        "activeButtonSecondaryFg": f.mix(on, "orange", 0.72),
        "activeLineFg": c.orange, "activeLineFgError": bad,
        "lightButtonBgOver": c.surface0, "lightButtonBgRipple": c.surface1,
        "attentionButtonFg": bad, "attentionButtonFgOver": bad,
        "attentionButtonBgOver": tint("red", 0.15), "attentionButtonBgRipple": tint("red", 0.28),
        "menuBg": paper, "menuBgOver": c.surface1 if dark else c.surface0,
        "menuBgRipple": c.surface2 if dark else c.surface1,
        "menuIconFg": c.overlay2, "menuIconFgOver": c.subtext1, "menuSubmenuArrowFg": c.overlay2,
        "menuFgDisabled": c.overlay0, "menuSeparatorFg": c.surface0,
        "scrollBarBg": _a(c.overlay0, 0.60), "scrollBarBgOver": _a(c.overlay1, 0.75),
        "scrollBg": _a(c.surface1, 0.35), "scrollBgOver": _a(c.surface1, 0.55),
        "smallCloseIconFg": c.overlay1, "smallCloseIconFgOver": c.subtext0,
        "radialFg": over_fg, "radialBg": _a(over_bg, 0.34),
        "placeholderFg": c.overlay1, "placeholderFgActive": c.overlay0,
        "inputBorderFg": c.surface1, "filterInputBorderFg": c.orange, "checkboxFg": c.overlay0,
        "botKbPrimaryBg": _a(c.orange, 0.80), "botKbDangerBg": _a(c.red, 0.80),
        "botKbSuccessBg": _a(c.green, 0.80), "botKbInlinePrimaryBg": _a(c.orange, 0.70),
        "botKbInlineDangerBg": _a(c.red, 0.70), "botKbInlineSuccessBg": _a(c.green, 0.70),
        "sliderBgInactive": c.surface1,
        "tooltipBg": paper, "tooltipFg": c.subtext1, "tooltipBorderFg": c.surface1,
        # title bar
        "titleShadow": _a(shade, 0.06), "titleBg": c.crust,
        "titleButtonFg": c.overlay1, "titleButtonBgOver": c.surface0, "titleButtonFgOver": c.subtext1,
        "titleButtonCloseBgOver": c.red, "titleButtonCloseFgOver": on_red,
        "titleFg": c.overlay1, "titleFgActive": c.subtext1,
        # tray
        "trayCounterBg": c.orange, "trayCounterBgMute": c.overlay1, "trayCounterFg": on,
        "trayCounterBgMacInvert": over_fg, "trayCounterFgMacInvert": _a(over_fg, 0.004),
        # layers and boxes
        "layerBg": _a(shade, 0.50),
        "boxTextFgGood": c.green, "boxTextFgError": bad, "boxTitleFg": c.text_hi,
        "boxTitleAdditionalFg": c.overlay2, "boxDividerBg": c.mantle,
        "paymentsTipActive": c.green,
        "contactsStatusFgOnline": c.green,
        "photoCropPointFg": _a(over_fg, 0.50),
        "callArrowFg": c.green, "callArrowMissedFg": bad,
        # intro: a soft sunset behind the paper plane
        "introCoverTopBg": tint("orange", 0.35), "introCoverBottomBg": tint("yellow", 0.30),
        "introCoverIconsFg": tint("yellow", 0.50), "introCoverPlaneTrace": _a(c.text_hi, 0.40),
        "introCoverPlaneInner": c.subtext1, "introCoverPlaneOuter": c.overlay2,
        "introCoverPlaneTop": c.text_hi,
        # chat list: espresso sidebar, orange marks what's new
        "dialogsBg": c.mantle, "dialogsBgOver": c.surface0, "dialogsBgActive": c.surface1,
        "dialogsRippleBg": c.surface1, "dialogsRippleBgActive": c.surface2,
        "dialogsTextFgService": c.subtext1, "dialogsDraftFg": bad,
        "dialogsSendingIconFg": c.overlay1, "dialogsSentIconFg": c.orange,
        "dialogsSentIconFgOver": c.orange,
        "dialogsUnreadBgMuted": c.overlay1, "dialogsArchiveFg": c.subtext0,
        "dialogsArchiveFgOver": c.subtext1, "dialogsOnlineBadgeFg": c.green,
        "dialogsNameFgActive": c.text_hi, "dialogsDateFgActive": c.subtext0,
        "dialogsTextFgActive": c.subtext1, "dialogsTextFgServiceActive": c.text,
        "dialogsDraftFgActive": bad, "dialogsVerifiedIconBgActive": c.orange,
        "dialogsVerifiedIconFgActive": on, "dialogsSendingIconFgActive": c.overlay2,
        "dialogsSentIconFgActive": c.orange, "dialogsUnreadBgActive": c.orange,
        "dialogsUnreadBgMutedActive": c.overlay1, "dialogsUnreadFgActive": on,
        "dialogsOnlineBadgeFgActive": c.green,
        "dialogsMentionIconFg": c.orange, "dialogsReactionIconFg": c.red_hi, "dialogsPollIconFg": c.clay,
        "searchedTextMatchBg": t["search"], "searchedTextMatchFg": c.text_hi,
        "searchedTextCurrentMatchBg": t["search_cur"], "searchedTextCurrentMatchFg": c.text_hi,
        # emoji and stickers
        "emojiPanCategories": c.mantle, "emojiPanHeaderBg": _a(c.base, 0.95),
        "emojiIconFg": c.overlay1, "emojiSubIconFgActive": c.subtext1,
        "stickerPanDeleteBg": c.crust, "stickerPanDeleteFg": over_fg,
        "stickerPreviewBg": _a(c.base, 0.69),
        "stickerPanPremium1": c.orange, "stickerPanPremium2": c.yellow,
        # history
        "historyLinkInFg": c.denim, "historyLinkOutFg": c.denim,
        "historyOutIconFg": c.orange, "historyOutIconFgSelected": c.orange_hi,
        "historyIconFgInverted": over_fg,
        "historySendingOutIconFg": c.overlay2, "historySendingInIconFg": c.overlay1,
        "historySendingInvertedIconFg": _a(over_fg, 0.78),
        "historyCallArrowInFg": c.green, "historyCallArrowInFgSelected": c.green,
        "historyUnreadBarBg": c.surface0, "historyUnreadBarFg": c.orange,
        "historyForwardChooseBg": _a(over_bg, 0.30), "historyForwardChooseFg": over_fg,
        "historyPeerUserpicFg": on,
        "historyPeerSavedMessagesBg": c.orange, "historyPeerSavedMessagesBg2": deep(c.orange),
        "settingsIconBg1": c.red_hi, "settingsIconBg2": c.green, "settingsIconBg3": c.yellow,
        "settingsIconBg4": c.sage, "settingsIconBg5": c.denim, "settingsIconBg6": c.clay,
        "settingsIconBg8": c.orange, "settingsIconBgArchive": c.overlay1, "settingsIconFg": on,
        "historyScrollBarBg": _a(c.overlay0, 0.60), "historyScrollBarBgOver": _a(c.overlay1, 0.75),
        "historyScrollBg": _a(c.surface1, 0.35), "historyScrollBgOver": _a(c.surface1, 0.55),
        # bubbles: incoming on coppertone, outgoing in a warm orange wash
        "msgInBg": c.surface0, "msgInBgSelected": c.surface1,
        "msgOutBg": out_bg, "msgOutBgSelected": out_sel,
        "msgSelectOverlay": _a(c.orange, 0.30), "msgStickerOverlay": _a(c.orange, 0.50),
        "msgOutServiceFg": c.orange, "msgOutServiceFgSelected": c.orange,
        "msgInShadow": _a(shade, 0.18), "msgInShadowSelected": _a(shade, 0.18),
        "msgOutShadow": _a(shade, 0.18), "msgOutShadowSelected": _a(shade, 0.18),
        "msgInDateFg": c.overlay1 if dark else c.overlay2, "msgInDateFgSelected": c.overlay2 if dark else c.subtext0,
        "msgOutDateFg": f.mix("orange", "overlay1", 0.40),
        "msgOutDateFgSelected": f.mix("orange", "overlay2", 0.50),
        "msgServiceFg": c.text, "msgServiceBg": _a(c.surface1, 0.85),
        "msgServiceBgSelected": _a(c.surface2, 0.90),
        "msgOutReplyBarColor": c.orange, "msgImgReplyBarColor": over_fg,
        "msgInMonoFg": c.green, "msgOutMonoFg": c.green,
        "msgDateImgFg": over_fg, "msgDateImgBg": _a(over_bg, 0.40),
        "msgDateImgBgOver": _a(over_bg, 0.55), "msgDateImgBgSelected": _a(c.orange, 0.55),
        "msgFileThumbLinkOutFg": c.orange, "msgFileThumbLinkOutFgSelected": c.orange_hi,
        "msgFileInBgOver": c.orange_hi, "msgFileInBgSelected": c.orange_hi,
        "msgFileOutBg": c.orange, "msgFileOutBgSelected": c.orange_hi,
        "historyFileThumbIconFg": over_fg, "historyFileThumbIconFgSelected": over_fg,
        "msgWaveformInActiveSelected": c.orange_hi,
        "msgWaveformInInactive": c.overlay0, "msgWaveformInInactiveSelected": c.overlay1,
        "msgWaveformOutActive": c.orange, "msgWaveformOutActiveSelected": c.orange_hi,
        "msgWaveformOutInactive": tint("orange", 0.45), "msgWaveformOutInactiveSelected": tint("orange", 0.55),
        "msgBotKbOverBgAdd": _a(c.text, 0.12), "msgBotKbIconFg": c.text, "msgBotKbRippleBg": _a(shade, 0.12),
        "youtubePlayIconBg": _a(c.red, 0.80), "youtubePlayIconFg": on_red,
        "videoPlayIconBg": _a(over_bg, 0.50), "videoPlayIconFg": over_fg,
        "toastBg": _a(c.surface1, 0.95) if dark else _a(night.mantle, 0.92),
        "toastFg": night.text_hi,
        "historyToDownBg": c.surface0, "historyToDownBgOver": c.surface1,
        "historyToDownBgRipple": c.surface2, "historyToDownShadow": _a(shade, 0.25),
        "historyComposeAreaBg": c.base, "historyComposeAreaFgService": c.overlay2,
        "historyComposeButtonBgOver": c.surface0, "historyComposeButtonBgRipple": c.surface1,
        "mapPointDrop": c.red_hi, "mapPointDot": over_fg,
        # shared media, profile, settings
        "overviewCheckBg": _a(over_bg, 0.25), "overviewCheckFgActive": on,
        "overviewPhotoSelectOverlay": _a(c.orange, 0.20),
        "profileStatusFgOver": c.subtext0,
        "notificationSampleCloseFg": c.surface2, "notificationSampleTextFg": c.surface2,
        "notificationSampleNameFg": c.overlay0,
        "mainMenuCoverBg": c.mantle, "mainMenuCloudBg": c.orange,
        "mediaPlayerDisabledFg": c.overlay0,
        # media viewer (always dark)
        "mediaviewFileRedCornerFg": c.red_hi, "mediaviewFileYellowCornerFg": c.yellow,
        "mediaviewFileGreenCornerFg": c.green, "mediaviewFileBlueCornerFg": c.denim,
        "mediaviewMenuBg": night.surface0, "mediaviewMenuBgOver": night.surface1,
        "mediaviewMenuBgRipple": night.surface2, "mediaviewMenuFg": night.text,
        "mediaviewBg": _a(night.crust, 0.92), "mediaviewVideoBg": night.crust,
        "mediaviewControlBg": _a(night.crust, 0.24), "mediaviewControlFg": night.text_hi,
        "mediaviewCaptionBg": _a(night.crust, 0.50), "mediaviewTextLinkFg": night.denim_hi,
        "mediaviewPlaybackActive": night.subtext1, "mediaviewPlaybackInactive": night.surface1,
        "mediaviewPlaybackActiveOver": night.text_hi, "mediaviewPlaybackInactiveOver": night.surface2,
        "mediaviewPlaybackProgressFg": _a(night.text_hi, 0.78),
        "mediaviewPlaybackIconRipple": _a(night.text_hi, 0.08),
        "mediaviewPipControlsFg": _a(night.text_hi, 0.85), "mediaviewPipControlsFgOver": night.text_hi,
        "mediaviewPipPlaybackActive": _a(night.text_hi, 0.85),
        "mediaviewPipPlaybackInactive": _a(night.text_hi, 0.15),
        "mediaviewTransparentBg": night.text, "mediaviewTransparentFg": night.subtext0,
        # calls (always dark)
        "callBg": _a(night.base, 0.95), "callBgOpaque": night.mantle, "callBgButton": _a(night.mantle, 0.50),
        "callNameFg": night.text_hi, "callStatusFg": night.overlay2,
        "callIconBg": _a(night.text_hi, 0.12), "callIconFg": night.text_hi,
        "callIconBgActive": _a(night.text_hi, 0.90), "callIconFgActive": night.crust,
        "callIconActiveRipple": night.subtext1,
        "callAnswerBg": night.green, "callAnswerRipple": deep(night.green, 0.80),
        "callAnswerBgOuter": _a(night.green, 0.15),
        "callHangupBg": night.red, "callHangupRipple": deep(night.red, 0.80),
        "callMuteRipple": _a(night.text_hi, 0.07),
        "groupCallBg": night.crust, "groupCallActiveFg": night.orange_hi,
        "groupCallMembersBg": night.mantle, "groupCallMembersBgOver": night.base,
        "groupCallMembersBgRipple": night.surface0, "groupCallMembersFg": night.text_hi,
        "groupCallMemberActiveIcon": night.green_hi, "groupCallMemberActiveStatus": night.green_hi,
        "groupCallMemberInactiveIcon": night.overlay1, "groupCallMemberInactiveStatus": night.denim_hi,
        "groupCallMemberMutedIcon": night.red_hi, "groupCallMemberNotJoinedStatus": night.overlay1,
        "groupCallIconFg": night.text_hi,
        "groupCallLive1": night.green, "groupCallLive2": night.sage,
        "groupCallMuted1": night.orange, "groupCallMuted2": night.yellow,
        "groupCallForceMutedBar1": night.clay, "groupCallForceMutedBar2": night.red,
        "groupCallForceMutedBar3": night.orange,
        "groupCallForceMuted1": night.clay, "groupCallForceMuted2": night.red, "groupCallForceMuted3": night.red_hi,
        "groupCallMenuBg": night.surface0, "groupCallMenuBgOver": night.surface1,
        "groupCallMenuBgRipple": night.surface2,
        "groupCallLeaveBg": _a(night.red, 0.50), "groupCallLeaveBgRipple": _a(night.red, 0.62),
        "groupCallVideoTextFg": _a(night.text_hi, 0.88), "groupCallVideoSubTextFg": _a(night.text_hi, 0.75),
        "callBarBg": c.green, "callBarMuteRipple": deep(c.green, 0.80), "callBarBgMuted": c.overlay1,
        "callBarFg": on,
        "importantTooltipFgLink": night.denim_hi,
        "outdatedFg": on, "outdateSoonBg": c.orange, "outdatedBg": c.red,
        "spellUnderline": _a(c.red_hi, 0.55),
        # wallet (legacy, always dark)
        "walletTitleBg": night.crust, "walletTitleButtonFg": night.overlay0,
        "walletTitleButtonBgOver": night.surface0, "walletTitleButtonFgOver": night.overlay2,
        "walletTopBg": night.mantle, "walletBalanceFg": night.text_hi, "walletSubBalanceFg": night.text,
        "walletTopLabelFg": night.overlay2, "walletTopIconRipple": _a(night.text_hi, 0.07),
        # folders side bar: tunnel-dark rail, the open folder a tab into the chat list
        "sideBarBg": c.crust, "sideBarBgActive": c.mantle, "sideBarBgRipple": c.surface0,
        "sideBarTextFg": c.overlay2, "sideBarTextFgActive": c.orange,
        "sideBarIconFg": c.overlay2, "sideBarIconFgActive": c.orange,
        "sideBarBadgeBg": c.orange, "sideBarBadgeBgMuted": c.overlay1, "sideBarBadgeFg": on,
        "songCoverOverlayFg": _a(over_bg, 0.40), "photoEditorItemBaseHandleFg": c.orange,
        # premium, stats, credits
        "premiumButtonBg1": c.yellow, "premiumButtonBg2": c.orange, "premiumButtonBg3": c.red,
        "premiumButtonFg": on,
        "premiumIconBg1": c.orange, "premiumIconBg2": c.red_hi, "premiumIconBg3": c.green,
        "statisticsChartInactive": _a(c.surface1, 0.60), "statisticsChartActive": _a(c.overlay0, 0.85),
        "statisticsChartLineBlue": c.denim, "statisticsChartLineGreen": c.green,
        "statisticsChartLineRed": c.red_hi, "statisticsChartLineGolden": c.yellow,
        "statisticsChartLineLightblue": c.denim_hi, "statisticsChartLineLightgreen": c.green_hi,
        "statisticsChartLineOrange": c.orange, "statisticsChartLineIndigo": c.sage_hi,
        "statisticsChartLinePurple": c.clay, "statisticsChartLineCyan": c.sage,
        "creditsBg1": c.yellow, "creditsBg2": c.yellow_hi, "creditsBg3": deep(c.yellow, 0.80),
        "creditsFg": c.yellow, "creditsStroke": c.orange, "currencyFg": c.denim,
        "rankAdminFg": c.green, "rankOwnerFg": c.clay,
    }
    # Group member names and userpics, in Telegram's slot order (red, green, yellow, blue,
    # purple, pink, sea, orange), each taken to its nearest Subway Seat color.
    for i, color in enumerate(peers, 1):
        m[f"historyPeer{i}NameFg"] = color
        m[f"historyPeer{i}UserpicBg"] = color
        m[f"historyPeer{i}UserpicBg2"] = deep(color)
    m["msgFile1Bg"], m["msgFile2Bg"], m["msgFile3Bg"], m["msgFile4Bg"] = c.denim, c.green, c.red_hi, c.yellow
    for i in range(1, 5):
        hue = m[f"msgFile{i}Bg"]
        m[f"msgFile{i}BgDark"] = deep(hue, 0.88)
        m[f"msgFile{i}BgOver"] = deep(hue, 0.78)
        m[f"msgFile{i}BgSelected"] = f.mix(hue, "orange", 0.70)
    return m


def _spec():
    for tok in SPEC.split():
        for sep in ("=", "|"):
            if sep in tok:
                key, ref = tok.split(sep)
                yield key, sep, ref
                break
        else:
            yield tok, "", None


def resolve(f):
    """Every palette key → #rrggbb[aa], in upstream order."""
    mapped = colors(f)
    spec = list(_spec())
    refs = {k: ref for k, _, ref in spec}
    known = set(refs)
    if unknown := set(mapped) - known:
        raise SystemExit(f"telegram: unknown palette keys {sorted(unknown)}")
    out = {}

    def get(key):
        if key not in out:
            if key in mapped:
                out[key] = mapped[key]
            elif refs[key] is not None:
                out[key] = get(refs[key])
            else:
                raise SystemExit(f"telegram: literal key {key} has no Subway Seat mapping")
        return out[key]

    return {k: get(k).lower() for k, _, _ in spec}


def png(color, size=64):
    """A solid size×size RGB PNG, for the bundled chat background."""
    r, g, b = p.hex_to_rgb(color)
    row = b"\x00" + bytes((r, g, b)) * size
    raw = zlib.compress(row * size, 9)

    def chunk(kind, data):
        return struct.pack(">I", len(data)) + kind + data + struct.pack(">I", zlib.crc32(kind + data))

    ihdr = struct.pack(">IIBBBBB", size, size, 8, 2, 0, 0, 0)
    return b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", ihdr) + chunk(b"IDAT", raw) + chunk(b"IEND", b"")


def theme_text(f):
    lines = [f"// {HEADER}", f"// {f.name} for Telegram Desktop", ""]
    lines += [f"{k}: {v};" for k, v in resolve(f).items()]
    return "\n".join(lines) + "\n"


def build(flavors):
    outs = []
    for f in flavors:
        text = theme_text(f)
        archive = zip_bytes({"colors.tdesktop-theme": text, "tiled.png": png(f.base)})
        outs.append(Out(f"{f.slug}.tdesktop-theme", archive, flavor=f.id, lang="text",
                        how="open it with Telegram Desktop, or Settings › Chat Settings › Choose from file"))
        outs.append(Out(f"{f.slug}/colors.tdesktop-theme", text, flavor=f.id, lang="text",
                        how=f"the palette inside {f.slug}.tdesktop-theme, for reading or editing"))
    return outs
