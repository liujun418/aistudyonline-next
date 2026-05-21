import Link from "next/link";

interface ToolCardProps {
  id: string;
  name: string;
  description: string;
  category: string;
  tags: string[];
  difficulty: "beginner" | "intermediate" | "advanced";
  url: string;
  rating: number;
  pricing: string;
  icon: string;
  locale: string;
  dict?: Record<string, unknown>;
}

const difficultyStyles: Record<string, string> = {
  beginner: "bg-green-100 text-green-700 dark:bg-green-900/40 dark:text-green-300",
  intermediate: "bg-amber-100 text-amber-700 dark:bg-amber-900/40 dark:text-amber-300",
  advanced: "bg-red-100 text-red-700 dark:bg-red-900/40 dark:text-red-300",
};

function getLabel(dict: Record<string, unknown> | undefined, key: string, fallback: string): string {
  const difficulty = (dict as any)?.tools?.difficulty;
  if (difficulty && difficulty[key]) return difficulty[key] as string;
  const fallbacks: Record<string, string> = {
    beginner: "Beginner",
    intermediate: "Intermediate",
    advanced: "Advanced",
    pricing: "Pricing",
    visit: "Visit",
  };
  return fallbacks[key] || fallback;
}

function StarRating({ rating }: { rating: number }) {
  return (
    <span className="inline-flex gap-0.5" aria-label={`${rating} out of 5 stars`}>
      {[1, 2, 3, 4, 5].map((star) => (
        <svg
          key={star}
          className={`h-4 w-4 ${star <= rating ? "text-amber-400" : "text-zinc-200 dark:text-zinc-600"}`}
          fill="currentColor"
          viewBox="0 0 20 20"
        >
          <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
        </svg>
      ))}
    </span>
  );
}

export default function ToolCard({
  id,
  name,
  description,
  tags,
  difficulty,
  url,
  rating,
  pricing,
  icon,
  locale,
  dict,
}: ToolCardProps) {
  const diffLabel = getLabel(dict, difficulty, difficulty.charAt(0).toUpperCase() + difficulty.slice(1));
  const pricingLabel = getLabel(dict, "pricing", "Pricing");
  const visitLabel = getLabel(dict, "visit", "Visit");

  return (
    <div className="flex flex-col rounded-xl border border-border bg-surface p-5 shadow-sm transition hover:shadow-md">
      {/* Icon + Name + Rating */}
      <div className="mb-3 flex items-start justify-between">
        <div className="flex items-center gap-3">
          <span className="text-2xl" role="img" aria-label={name}>
            {icon}
          </span>
          <div>
            <h3 className="text-sm font-semibold text-foreground">{name}</h3>
            <StarRating rating={rating} />
          </div>
        </div>
        <span
          className={`shrink-0 rounded-full px-2.5 py-0.5 text-xs font-medium ${difficultyStyles[difficulty]}`}
        >
          {diffLabel}
        </span>
      </div>

      {/* Description */}
      <p className="mb-3 flex-1 text-sm leading-relaxed text-zinc-600 dark:text-zinc-400">
        {description}
      </p>

      {/* Tags */}
      {tags.length > 0 && (
        <div className="mb-3 flex flex-wrap gap-1.5">
          {tags.slice(0, 3).map((tag) => (
            <span
              key={tag}
              className="rounded-md bg-primary-100 px-2 py-0.5 text-xs text-primary-700 dark:bg-primary-900/40 dark:text-primary-300"
            >
              {tag}
            </span>
          ))}
        </div>
      )}

      {/* Pricing */}
      <div className="mb-4 text-xs text-zinc-500 dark:text-zinc-400">
        <span className="font-medium">{pricingLabel}:</span> {pricing}
      </div>

      {/* Visit link */}
      <Link
        href={url}
        target="_blank"
        rel="noopener noreferrer"
        className="inline-flex items-center gap-1 self-start rounded-lg bg-primary-500 px-4 py-2 text-sm font-medium text-white transition hover:bg-primary-600"
      >
        {visitLabel}
        <svg className="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M14 5l7 7m0 0l-7 7m7-7H3" />
        </svg>
      </Link>
    </div>
  );
}
