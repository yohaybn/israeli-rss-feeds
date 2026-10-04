import test from 'node:test';
import assert from 'node:assert/strict';
import { trigger } from './trigger.mjs';

const json = (body, status = 200) => ({ ok: status < 400, status, json: async () => body });

test('dispatches when no run is active', async () => {
  const calls = [];
  const f = async (url, opts = {}) => {
    calls.push([opts.method || 'GET', url]);
    return url.includes('/runs?') ? json({ total_count: 0 }) : { ok: true, status: 204 };
  };
  assert.equal(await trigger({ GH_TOKEN: 't' }, f), 'dispatched');
  assert.equal(calls.at(-1)[0], 'POST');
});

test('skips when a run is active', async () => {
  const f = async (url) => json({ total_count: 1 });
  assert.match(await trigger({ GH_TOKEN: 't' }, f), /skipped/);
});

test('fails without a token', async () => {
  await assert.rejects(() => trigger({}, async () => json({})), /GH_TOKEN/);
});
