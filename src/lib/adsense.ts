import { ADSENSE_PUBLISHER_ID } from "@/lib/constants";

export const ADSENSE_SLOTS = {
  rectangle: "7831293092",  // 300×250 — sidebar, inline
  horizontal: "8266407367", // 728×90 — full-width, between sections
} as const;

export const ADSENSE_CONFIG = {
  publisherId: ADSENSE_PUBLISHER_ID,
};
