document.addEventListener('DOMContentLoaded', () => {
    const homeView =
        document.getElementById('home-view');

    const resultsContainer =
        document.getElementById('search-results-container');

    const searchForm =
        document.getElementById('search-form');

    const searchInput =
        document.getElementById('search');

    const resultsList =
        document.getElementById('results-list');

    const resultsHeading =
        document.getElementById('results-heading');

    const backButton =
        document.getElementById('back-to-home');

    const siteLogo =
        document.querySelector('.site-logo');

    let allSearchData = [];
    let loadPromise = null;

    function escapeHtml(str) {
        if (!str) return '';

        return String(str)
            .replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')
            .replace(/"/g, '&quot;')
            .replace(/'/g, '&#039;');
    }

    async function loadData() {
        if (loadPromise) {
            return loadPromise;
        }

        loadPromise = (async () => {
            try {
                const [
                    learnRes,
                    refRes
                ] = await Promise.all([
                    fetch('json/learn.json')
                        .catch(error => {
                            console.error(
                                'Error loading learn.json:',
                                error
                            );

                            return {
                                ok: false
                            };
                        }),

                    fetch('json/references.json')
                        .catch(error => {
                            console.error(
                                'Error loading references.json:',
                                error
                            );

                            return {
                                ok: false
                            };
                        })
                ]);

                const items = [];

                if (learnRes.ok) {
                    const learnData =
                        await learnRes.json();

                    if (
                        learnData &&
                        Array.isArray(
                            learnData.chapters
                        )
                    ) {
                        learnData.chapters.forEach(
                            chapter => {
                                const chapterName =
                                    chapter.name || '';

                                const chapterId =
                                    chapter.id != null
                                        ? chapter.id
                                        : '';

                                if (
                                    Array.isArray(
                                        chapter.items
                                    )
                                ) {
                                    chapter.items.forEach(
                                        item => {
                                            items.push({
                                                title:
                                                    item.id
                                                        ? `${item.id} - ${item.name}`
                                                        : (
                                                            item.name || ''
                                                        ),

                                                name:
                                                    item.name || '',

                                                id:
                                                    item.id || '',

                                                chapterName:
                                                    chapterName,

                                                chapterId:
                                                    chapterId,

                                                category:
                                                    'Learn',

                                                description:
                                                    item.description || '',

                                                url:
                                                    item.url || ''
                                            });
                                        }
                                    );
                                }
                            }
                        );
                    }
                }

                if (refRes.ok) {
                    const refData =
                        await refRes.json();

                    if (Array.isArray(refData)) {
                        refData.forEach(item => {
                            items.push({
                                title:
                                    item.title || '',

                                name:
                                    item.title || '',

                                id: '',

                                chapterName: '',

                                chapterId: '',

                                category:
                                    'Reference',

                                description:
                                    item.description || '',

                                url:
                                    item.url || ''
                            });
                        });
                    }
                }

                allSearchData = items;

                return allSearchData;

            } catch (error) {
                console.error(
                    'Error initializing search data:',
                    error
                );

                return [];
            }
        })();

        return loadPromise;
    }

    function searchItems(query) {
        const rawQuery =
            (query || '').trim();

        if (!rawQuery) {
            return allSearchData;
        }

        const q =
            rawQuery.toLowerCase();

        const queryTokens =
            q
                .split(/\s+/)
                .filter(Boolean);

        const scored = [];

        for (const item of allSearchData) {
            const titleLower =
                item.title.toLowerCase();

            const descLower =
                item.description.toLowerCase();

            const catLower =
                item.category.toLowerCase();

            const chapterLower =
                (
                    item.chapterName || ''
                ).toLowerCase();

            const idLower =
                (
                    item.id || ''
                ).toLowerCase();

            const combinedText =
                `${titleLower} ${descLower} ${catLower} ${chapterLower} ${idLower}`;

            const allTokensMatch =
                queryTokens.every(
                    token =>
                        combinedText.includes(token)
                );

            if (
                !allTokensMatch &&
                !combinedText.includes(q)
            ) {
                continue;
            }

            let score = 0;

            if (
                titleLower === q ||
                idLower === q
            ) {
                score += 100;

            } else if (
                titleLower.startsWith(q)
            ) {
                score += 60;

            } else if (
                titleLower.includes(q)
            ) {
                score += 40;
            }

            for (const token of queryTokens) {
                if (
                    titleLower.includes(token)
                ) {
                    score += 15;
                }

                if (
                    idLower === token
                ) {
                    score += 20;
                }

                if (
                    descLower.includes(token)
                ) {
                    score += 5;
                }

                if (
                    chapterLower.includes(token)
                ) {
                    score += 5;
                }

                if (
                    catLower.includes(token)
                ) {
                    score += 3;
                }
            }

            scored.push({
                item,
                score
            });
        }

        scored.sort((a, b) => {
            if (
                b.score !== a.score
            ) {
                return b.score - a.score;
            }

            return a.item.title.localeCompare(
                b.item.title
            );
        });

        return scored.map(
            result => result.item
        );
    }

    function renderResults(results, query) {
        const rawQuery =
            (query || '').trim();

        if (rawQuery) {
            resultsHeading.textContent =
                `Search Results for "${rawQuery}" (${results.length})`;

        } else {
            resultsHeading.textContent =
                `All Results (${results.length})`;
        }

        if (results.length === 0) {
            resultsList.innerHTML =
                `<p class="no-results">
                    No matches found for
                    "${escapeHtml(rawQuery)}".
                </p>`;

            return;
        }

        resultsList.innerHTML =
            results
                .map(item => `
                    <a
                        href="${escapeHtml(item.url)}"
                        class="learn-item"
                    >
                        <div class="result-header">

                            <h2>
                                ${escapeHtml(item.title)}
                            </h2>

                            <span class="meta-tag">
                                ${escapeHtml(item.category)}
                            </span>

                        </div>

                        ${
                            item.description
                                ? `
                                    <p>
                                        ${escapeHtml(
                                            item.description
                                        )}
                                    </p>
                                `
                                : ''
                        }

                    </a>
                `)
                .join('');
    }

    async function performSearch(
        query,
        updateHistory = true
    ) {
        await loadData();

        const results =
            searchItems(query);

        renderResults(
            results,
            query
        );

        homeView.style.display =
            'none';

        resultsContainer.style.display =
            'block';

        if (updateHistory) {
            const trimmed =
                (query || '').trim();

            const newUrl =
                trimmed
                    ? `index.html?q=${encodeURIComponent(trimmed)}`
                    : 'index.html';

            history.pushState(
                {
                    view: 'search',
                    query: trimmed
                },
                '',
                newUrl
            );
        }
    }

    function showHomeView(
        updateHistory = true
    ) {
        resultsContainer.style.display =
            'none';

        homeView.style.display =
            'block';

        searchInput.value = '';

        if (updateHistory) {
            history.pushState(
                {
                    view: 'home'
                },
                '',
                'index.html'
            );
        }
    }

    searchForm.addEventListener(
        'submit',
        event => {
            event.preventDefault();

            const query =
                searchInput.value;

            performSearch(
                query,
                true
            );
        }
    );

    backButton.addEventListener(
        'click',
        event => {
            event.preventDefault();

            showHomeView(true);
        }
    );

    siteLogo.addEventListener(
        'click',
        event => {
            if (
                resultsContainer.style.display ===
                'block'
            ) {
                event.preventDefault();

                showHomeView(true);
            }
        }
    );

    window.addEventListener(
        'popstate',
        () => {
            const params =
                new URLSearchParams(
                    window.location.search
                );

            const query =
                params.get('q');

            if (
                query !== null &&
                query !== ''
            ) {
                searchInput.value =
                    query;

                performSearch(
                    query,
                    false
                );
            } else {
                showHomeView(false);
            }
        }
    );

    loadData();

    const params =
        new URLSearchParams(
            window.location.search
        );

    const initialQuery =
        params.get('q');

    if (
        initialQuery !== null &&
        initialQuery !== ''
    ) {
        searchInput.value =
            initialQuery;

        performSearch(
            initialQuery,
            false
        );
    }
});