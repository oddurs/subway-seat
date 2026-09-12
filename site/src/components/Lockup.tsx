import * as stylex from "@stylexjs/stylex";
import { font } from "@/theme/type.stylex";

/**
 * The wordmark, in each city's own naming device.
 *
 * New York and London name things with a badge: the route bullet and the
 * roundel are both a shape you read before you read the word, and the lockup is
 * that shape set beside Helvetica. Paris has never worked that way. The Metro
 * names a station with a plate — an enamel panel with a keyline ruled inside
 * its edge and the name in caps within the keyline — and it is the frame, not
 * any mark, that tells you what you are looking at. So Paris gets a plate, and
 * the brass it would have spent on a badge goes into the keyline instead.
 *
 * That keeps the rule the nav is built on: one city colour in the band, spent
 * on the one object that city uses to name things. All three are drawn and CSS
 * shows the active family's, so the lockup is right in the first painted frame.
 *
 * Every variant's margin box is SIZE tall, which is what holds the band to one
 * height across the three cities — see Nav.
 */
export function Lockup() {
  return (
    <>
      <span data-only="new-york" {...stylex.props(styles.badge)}>
        <span aria-hidden {...stylex.props(styles.bullet)}>
          S
        </span>
        <span {...stylex.props(styles.word)}>Subway Seat</span>
      </span>

      <span data-only="london" {...stylex.props(styles.badge)}>
        <span aria-hidden {...stylex.props(styles.roundel)}>
          <span {...stylex.props(styles.ring)} />
          <span {...stylex.props(styles.bar)} />
        </span>
        <span {...stylex.props(styles.word)}>Subway Seat</span>
      </span>

      <span data-only="paris" {...stylex.props(styles.plate)}>
        <span aria-hidden {...stylex.props(styles.keyline)} />
        <span {...stylex.props(styles.plateWord)}>Subway Seat</span>
      </span>
    </>
  );
}

/** The lockup's height, and so the band's. */
const SIZE = 24;
/**
 * The plate stands proud of the row: it is the whole lockup, badge and wordmark
 * at once, so it takes the room both would have. The negative margin keeps its
 * margin box at SIZE, which is what holds the band to one height; the extra
 * 3px top and bottom is overflow into the band's air, which has 20 to spare.
 */
const PLATE = 30;

const styles = stylex.create({
  badge: {
    display: "flex",
    gap: 11,
    alignItems: "center",
    height: SIZE,
  },
  word: {
    fontSize: font.sizeMark,
    fontWeight: 700,
    lineHeight: font.leadFlat,
    color: "var(--sign-text)",
    letterSpacing: font.trackMark,
  },

  bullet: {
    display: "grid",
    placeItems: "center",
    width: SIZE,
    height: SIZE,
    fontSize: 14,
    fontWeight: 700,
    lineHeight: 1,
    color: "var(--sign-mark-alt)",
    backgroundColor: "var(--sign-mark)",
    borderRadius: "50%",
  },
  roundel: {
    position: "relative",
    display: "grid",
    placeItems: "center",
    width: SIZE,
    height: SIZE,
  },
  ring: {
    position: "absolute",
    inset: 0,
    borderColor: "var(--sign-mark)",
    borderStyle: "solid",
    // The Underground's ring is about a seventh of its diameter.
    borderWidth: 3.5,
    borderRadius: "50%",
  },
  // The bar runs past the ring on both sides — that overhang is most of what
  // makes a roundel read as a roundel and not as a disc.
  bar: {
    position: "relative",
    width: "128%",
    height: 5,
    backgroundColor: "var(--sign-mark-alt)",
  },

  // An enamel plate. Two edges, not one: the panel's own, and the keyline ruled
  // inside it. A single rounded outline would be a button; it is the second
  // line, and the margin of glaze it leaves, that reads as a plate.
  plate: {
    position: "relative",
    display: "flex",
    alignItems: "center",
    height: PLATE,
    // A plate is always wider than its name needs; the field around the word is
    // most of what separates a station sign from a label.
    paddingInline: 18,
    marginBlock: (SIZE - PLATE) / 2,
    backgroundColor: "color-mix(in srgb, var(--sign-text) 7%, var(--sign-bg))",
    // Vitreous enamel is glass: it takes the light along its top edge and goes
    // flat below. Without that it is a rounded rectangle with a border on it.
    backgroundImage: `linear-gradient(180deg,
      color-mix(in srgb, var(--sign-text) 7%, transparent),
      transparent 58%)`,
    boxShadow: "inset 0 1px 0 color-mix(in srgb, var(--sign-text) 13%, transparent)",
    // A plate's corner is a pressing radius, not a card's. Half the family's.
    borderRadius: "calc(var(--radius-card) / 2)",
  },
  keyline: {
    position: "absolute",
    inset: 4,
    borderColor: "color-mix(in srgb, var(--sign-mark) 88%, transparent)",
    borderStyle: "solid",
    borderWidth: 1,
    borderRadius: "calc(var(--radius-card) / 2 - 4px)",
  },
  // Caps, because a Metro plate has never carried anything else.
  plateWord: {
    position: "relative",
    fontSize: 14,
    fontWeight: 600,
    lineHeight: font.leadFlat,
    color: "var(--sign-text)",
    textTransform: "uppercase",
    letterSpacing: "0.13em",
    // Tracked caps sit off-centre by half their tracking: the last letter's
    // trailing space is inside the box, the first letter's is not.
    marginRight: "-0.13em",
  },
});
