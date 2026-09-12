import { type ColorName, families } from "@/lib/palette";

/**
 * What a role is called, in whichever city you're riding — `base` is Paneling
 * in New York and Moquette in London. Every family's name is rendered and CSS
 * shows the active one, the same way flavor-specific content works elsewhere,
 * so the page stays static.
 */
export function RoleName({ role }: { role: ColorName }) {
  return (
    <>
      {families.map((fam) => (
        <span key={fam.id} data-only={fam.id}>
          {fam.roleNames[role] ?? role}
        </span>
      ))}
    </>
  );
}
