// Cloudflare Worker (free tier): every 30 minutes, ask GitHub to run the publish workflow.
// Secret GH_TOKEN: fine-grained token for yohaybn/israeli-rss-feeds only, Actions: read and write.
const REPO = 'yohaybn/israeli-rss-feeds';
const WORKFLOW = 'generate-feeds.yml';
const API = `https://api.github.com/repos/${REPO}/actions/workflows/${WORKFLOW}`;

function headers(token) {
  return {
    Authorization: `Bearer ${token}`,
    Accept: 'application/vnd.github+json',
    'X-GitHub-Api-Version': '2022-11-28',
    'User-Agent': 'israeli-rss-feeds-cron-trigger',
  };
}

// Skip when a run is already queued or running, so triggers never stack.
export async function activeRuns(token, fetchFn = fetch) {
  let total = 0;
  for (const status of ['in_progress', 'queued']) {
    const r = await fetchFn(`${API}/runs?status=${status}&per_page=1`, { headers: headers(token) });
    if (!r.ok) throw new Error(`list runs (${status}) failed: ${r.status}`);
    total += (await r.json()).total_count || 0;
  }
  return total;
}

export async function trigger(env, fetchFn = fetch) {
  if (!env.GH_TOKEN) throw new Error('GH_TOKEN secret is not set');
  if (await activeRuns(env.GH_TOKEN, fetchFn) > 0) return 'skipped: a run is already active';
  const r = await fetchFn(`${API}/dispatches`, {
    method: 'POST',
    headers: { ...headers(env.GH_TOKEN), 'Content-Type': 'application/json' },
    body: JSON.stringify({ ref: 'main' }),
  });
  if (r.status !== 204) throw new Error(`dispatch failed: ${r.status}`);
  return 'dispatched';
}

export default {
  async scheduled(_event, env, ctx) {
    ctx.waitUntil(trigger(env).then((m) => console.log(m)));
  },
  // No public trigger: any request just reports that the worker exists.
  async fetch() {
    return new Response('cron trigger worker', { status: 200 });
  },
};
