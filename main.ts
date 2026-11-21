// news-image-20261120 entry (Node 22, standard library only).
//
// The entry is the infographic in entry.png beside this file: one image
// summing up Friday 20 November 2026's world news, drawn by draw_news.py
// (Pillow plus the Noto fonts) from the day's news digests. The grader
// runs this program in a fresh container with no network, the repository
// read-only at /bot and a writable /output; the program copies the image
// there. Both runs must write the same bytes, and a copy always does.
//
// Run it outside the grader with:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const here = dirname(fileURLToPath(import.meta.url));
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
mkdirSync(outDir, { recursive: true });
copyFileSync(join(here, 'entry.png'), join(outDir, 'entry.png'));
