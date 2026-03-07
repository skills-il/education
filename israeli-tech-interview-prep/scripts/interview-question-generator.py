#!/usr/bin/env python3
"""
Israeli Tech Interview Question Generator

Generate practice interview questions tailored to specific companies,
roles, difficulty levels, and topics for Israeli tech interviews.

Usage:
    python interview-question-generator.py --company wix --role backend --difficulty medium
    python interview-question-generator.py --role fullstack --difficulty hard --topic system-design
    python interview-question-generator.py --list-companies
    python interview-question-generator.py --list-topics
"""

import argparse
import json
import random
import sys
from dataclasses import dataclass, field
from typing import List, Optional, Dict


@dataclass
class InterviewQuestion:
    """Represents a single interview question."""
    title: str
    category: str  # coding, system-design, behavioral
    difficulty: str  # easy, medium, hard
    problem: str
    hints: List[str]
    solution_approach: str
    complexity: str
    follow_ups: List[str]
    common_mistakes: List[str]
    relevant_companies: List[str]
    tags: List[str]


# Question bank organized by category and difficulty
CODING_QUESTIONS: Dict[str, List[dict]] = {
    "easy": [
        {
            "title": "Two Sum with Sorted Array",
            "problem": (
                "Given a sorted array of integers and a target sum, find two numbers "
                "that add up to the target. Return their indices.\n\n"
                "Example: arr = [1, 3, 5, 7, 11], target = 10 -> [1, 3] (3 + 7 = 10)\n\n"
                "Constraint: The array is already sorted. Can you do better than O(n^2)?"
            ),
            "hints": [
                "Since the array is sorted, think about using two pointers.",
                "Start one pointer at the beginning and one at the end.",
                "If the sum is too large, move the right pointer left. If too small, move the left pointer right."
            ],
            "solution_approach": (
                "Two-pointer approach: Initialize left=0, right=len(arr)-1. "
                "While left < right, check if arr[left] + arr[right] == target. "
                "If sum is less, increment left. If greater, decrement right."
            ),
            "complexity": "Time: O(n), Space: O(1)",
            "follow_ups": [
                "What if the array is not sorted?",
                "What if there are multiple pairs that sum to the target?",
                "What if you need to find three numbers that sum to the target?"
            ],
            "common_mistakes": [
                "Using a hash map when two pointers is more efficient for sorted input",
                "Not handling the case where no pair exists",
                "Off-by-one errors with pointer bounds"
            ],
            "relevant_companies": ["all"],
            "tags": ["arrays", "two-pointers", "sorting"]
        },
        {
            "title": "Valid Parentheses",
            "problem": (
                "Given a string containing only '(', ')', '{', '}', '[' and ']', "
                "determine if the input string is valid.\n\n"
                "A string is valid if:\n"
                "- Open brackets are closed by the same type\n"
                "- Open brackets are closed in the correct order\n\n"
                "Examples: '()[]{}' -> true, '(]' -> false, '([)]' -> false, '{[]}' -> true"
            ),
            "hints": [
                "Think about what data structure is good for matching pairs in order.",
                "A stack (LIFO) is perfect for matching the most recent opening bracket.",
                "Push opening brackets, pop and compare when you see a closing bracket."
            ],
            "solution_approach": (
                "Use a stack. For each character: if opening bracket, push to stack. "
                "If closing bracket, check if stack is empty (invalid) or if top of stack "
                "matches (pop and continue). At the end, stack should be empty."
            ),
            "complexity": "Time: O(n), Space: O(n)",
            "follow_ups": [
                "What if the string also contains other characters (ignore them)?",
                "What if you need to find the minimum number of brackets to remove to make it valid?",
                "Can you solve it without a stack using O(1) space? (Only for single bracket type)"
            ],
            "common_mistakes": [
                "Forgetting to check if the stack is empty before popping",
                "Not checking that the stack is empty at the end",
                "Not handling edge cases like empty string or single bracket"
            ],
            "relevant_companies": ["all"],
            "tags": ["stack", "string", "parsing"]
        },
        {
            "title": "Reverse a Linked List",
            "problem": (
                "Given the head of a singly linked list, reverse it in-place and return "
                "the new head.\n\n"
                "Example: 1 -> 2 -> 3 -> 4 -> 5 becomes 5 -> 4 -> 3 -> 2 -> 1\n\n"
                "Can you solve it both iteratively and recursively?"
            ),
            "hints": [
                "For iterative: use three pointers (prev, current, next).",
                "At each step, save the next node, point current.next to prev, then advance.",
                "For recursive: the base case is when you reach the last node."
            ],
            "solution_approach": (
                "Iterative: Initialize prev=None, current=head. While current is not None: "
                "save next=current.next, set current.next=prev, advance prev=current, "
                "current=next. Return prev as new head."
            ),
            "complexity": "Time: O(n), Space: O(1) iterative / O(n) recursive",
            "follow_ups": [
                "Reverse only a portion of the list (from position m to n)",
                "Reverse in groups of k",
                "What if it's a doubly linked list?"
            ],
            "common_mistakes": [
                "Losing the reference to the next node before reversing the pointer",
                "Not returning the correct new head",
                "Stack overflow with recursive approach on very long lists"
            ],
            "relevant_companies": ["all"],
            "tags": ["linked-list", "pointers", "recursion"]
        },
    ],
    "medium": [
        {
            "title": "LRU Cache Implementation",
            "problem": (
                "Design and implement a Least Recently Used (LRU) cache.\n\n"
                "Operations:\n"
                "- get(key): Return the value if key exists, otherwise -1\n"
                "- put(key, value): Insert or update. If cache is at capacity, "
                "evict the least recently used item.\n\n"
                "Both operations must be O(1) time complexity.\n\n"
                "Example:\n"
                "cache = LRUCache(2)\n"
                "cache.put(1, 1)\n"
                "cache.put(2, 2)\n"
                "cache.get(1)    -> 1\n"
                "cache.put(3, 3) -> evicts key 2\n"
                "cache.get(2)    -> -1"
            ),
            "hints": [
                "You need O(1) lookup AND O(1) insertion/deletion.",
                "A hash map gives O(1) lookup. What gives O(1) ordered insertion/deletion?",
                "Combine a hash map with a doubly linked list. Map keys to list nodes."
            ],
            "solution_approach": (
                "Use a hash map (key -> node) + doubly linked list. "
                "On get: move node to front of list. On put: if exists, update and move to front. "
                "If new and at capacity, remove from tail of list and delete from map. "
                "Add new node to front."
            ),
            "complexity": "Time: O(1) for both operations, Space: O(capacity)",
            "follow_ups": [
                "How would you make this thread-safe?",
                "How would you implement an LFU (Least Frequently Used) cache?",
                "How would you implement TTL (time-to-live) for entries?"
            ],
            "common_mistakes": [
                "Not updating the position on get (only on put)",
                "Not handling the case where put updates an existing key",
                "Memory leaks from not properly removing evicted nodes"
            ],
            "relevant_companies": ["wix", "monday", "google", "meta", "amazon"],
            "tags": ["hash-map", "linked-list", "design", "cache"]
        },
        {
            "title": "Rate Limiter",
            "problem": (
                "Implement a rate limiter that allows at most N requests per time window T.\n\n"
                "Interface:\n"
                "- RateLimiter(max_requests, window_seconds)\n"
                "- allow(timestamp): Returns True if the request should be allowed\n\n"
                "Example:\n"
                "limiter = RateLimiter(3, 60)  # 3 requests per 60 seconds\n"
                "limiter.allow(1)   -> True\n"
                "limiter.allow(20)  -> True\n"
                "limiter.allow(40)  -> True\n"
                "limiter.allow(50)  -> False (3 requests within 60s window)\n"
                "limiter.allow(61)  -> True (first request expired)"
            ),
            "hints": [
                "Think about a sliding window approach.",
                "You need to track timestamps of recent requests.",
                "A queue (deque) can efficiently manage the window of timestamps."
            ],
            "solution_approach": (
                "Use a deque of timestamps. On each allow() call: remove timestamps older "
                "than (current_time - window). Then check if len(deque) < max_requests. "
                "If yes, add timestamp and return True. Otherwise return False."
            ),
            "complexity": "Time: O(1) amortized, Space: O(max_requests)",
            "follow_ups": [
                "How would you implement this in a distributed system?",
                "What about token bucket vs. sliding window algorithms?",
                "How would you handle rate limiting per user AND per API endpoint?",
                "How would you implement this with Redis?"
            ],
            "common_mistakes": [
                "Not cleaning up expired timestamps efficiently",
                "Using a list instead of a deque (O(n) removal from front)",
                "Not handling the edge case where window_seconds is 0"
            ],
            "relevant_companies": ["checkpoint", "snyk", "appsflyer", "wix"],
            "tags": ["design", "queue", "sliding-window", "system-design"]
        },
        {
            "title": "Find All Anagram Groups",
            "problem": (
                "Given a list of strings, group all anagrams together.\n\n"
                "Example:\n"
                "Input: ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']\n"
                "Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]\n\n"
                "Note: Order within groups and between groups does not matter."
            ),
            "hints": [
                "Two strings are anagrams if they have the same characters in the same frequencies.",
                "What if you sort each string? Anagrams will have the same sorted form.",
                "Use a hash map with sorted string as key."
            ],
            "solution_approach": (
                "Create a hash map where key = sorted string, value = list of original strings. "
                "For each string, sort it and add the original to the corresponding list. "
                "Return all values from the map."
            ),
            "complexity": "Time: O(n * k log k) where k is max string length, Space: O(n * k)",
            "follow_ups": [
                "Can you solve it without sorting? (Use character frequency as the key)",
                "What if strings are very long? Is there a more efficient key?",
                "How would you find anagrams in a stream of strings?"
            ],
            "common_mistakes": [
                "Using the wrong key type for the hash map",
                "Not considering Unicode or case sensitivity",
                "Inefficient key generation for very long strings"
            ],
            "relevant_companies": ["all"],
            "tags": ["hash-map", "string", "sorting"]
        },
    ],
    "hard": [
        {
            "title": "Design a Task Scheduler",
            "problem": (
                "Given a list of tasks (represented by characters) and a cooldown period n, "
                "find the minimum time to execute all tasks.\n\n"
                "Rules:\n"
                "- Each task takes 1 unit of time\n"
                "- Between two same tasks, there must be at least n units of cooldown\n"
                "- During cooldown, you can execute other tasks or idle\n\n"
                "Example:\n"
                "tasks = ['A','A','A','B','B','B'], n = 2\n"
                "Output: 8\n"
                "Explanation: A -> B -> idle -> A -> B -> idle -> A -> B"
            ),
            "hints": [
                "Think about the most frequent task first. It creates the framework.",
                "The minimum time is determined by the most frequent task and the cooldown.",
                "Formula: (max_freq - 1) * (n + 1) + count_of_tasks_with_max_freq.",
                "But the answer is at least len(tasks) (when no idle time is needed)."
            ],
            "solution_approach": (
                "Count frequencies. The most frequent task(s) determine the minimum time. "
                "Formula: result = (max_freq - 1) * (n + 1) + num_tasks_with_max_freq. "
                "Answer is max(result, len(tasks)) since we never need fewer slots than tasks."
            ),
            "complexity": "Time: O(n), Space: O(1) (at most 26 unique tasks)",
            "follow_ups": [
                "What if tasks have different execution times?",
                "What if you need to return the actual schedule, not just the time?",
                "How would you implement this for a real job scheduler with priorities?"
            ],
            "common_mistakes": [
                "Not considering the case where len(tasks) > calculated minimum",
                "Overcomplicating with a priority queue when math formula suffices",
                "Not counting all tasks that share the maximum frequency"
            ],
            "relevant_companies": ["monday", "wix", "google", "amazon"],
            "tags": ["greedy", "math", "scheduling"]
        },
        {
            "title": "Consistent Hashing Ring",
            "problem": (
                "Implement a consistent hashing ring for distributing keys across nodes.\n\n"
                "Operations:\n"
                "- add_node(node_id): Add a node to the ring\n"
                "- remove_node(node_id): Remove a node from the ring\n"
                "- get_node(key): Return which node a key maps to\n\n"
                "Requirements:\n"
                "- When a node is added/removed, only K/N keys should be remapped "
                "(K = total keys, N = total nodes)\n"
                "- Support virtual nodes for better distribution"
            ),
            "hints": [
                "Hash both nodes and keys to positions on a ring (0 to 2^32-1).",
                "For get_node, find the first node position >= hash(key) on the ring.",
                "Virtual nodes: each physical node gets multiple positions on the ring.",
                "Use a sorted data structure for efficient lookup."
            ],
            "solution_approach": (
                "Use a sorted array of (hash_position, node_id) pairs. "
                "add_node: insert V virtual nodes at hash(node_id + '_' + i) positions. "
                "remove_node: remove all virtual nodes for that node. "
                "get_node: binary search for the first position >= hash(key), wrap around if needed."
            ),
            "complexity": "Time: O(log(N*V)) for get, O(N*V) for add/remove. Space: O(N*V)",
            "follow_ups": [
                "How would you handle node weights (some nodes handle more traffic)?",
                "How does this relate to distributed databases like Cassandra or DynamoDB?",
                "What happens during a node failure? How do you handle replication?",
                "How would you implement bounded load consistent hashing?"
            ],
            "common_mistakes": [
                "Not handling the wrap-around case (when key hash > all node hashes)",
                "Using too few virtual nodes (causes uneven distribution)",
                "Not considering hash collisions"
            ],
            "relevant_companies": ["appsflyer", "taboola", "outbrain", "google", "amazon"],
            "tags": ["distributed-systems", "hashing", "design"]
        },
    ],
}

SYSTEM_DESIGN_QUESTIONS: List[dict] = [
    {
        "title": "Design a Real-Time Collaborative Editor",
        "difficulty": "hard",
        "problem": (
            "Design a system like Google Docs that supports real-time collaborative "
            "editing with multiple users working on the same document simultaneously.\n\n"
            "Requirements:\n"
            "- Multiple users editing the same document in real-time\n"
            "- Conflict resolution when two users edit the same section\n"
            "- Offline support with sync when back online\n"
            "- Version history and undo\n"
            "- Scale to 10M+ documents, 100K concurrent editors"
        ),
        "hints": [
            "Consider OT (Operational Transform) vs. CRDT for conflict resolution",
            "WebSocket for real-time communication",
            "Event sourcing for version history"
        ],
        "solution_approach": (
            "Key components: WebSocket gateway for real-time connection, "
            "CRDT or OT engine for conflict resolution, document service for persistence, "
            "Redis pub/sub for cross-server communication, S3 for document storage, "
            "PostgreSQL for metadata. Use event sourcing for version history."
        ),
        "follow_ups": [
            "How would you handle a network partition?",
            "How would you implement cursor presence (seeing other users' cursors)?",
            "How would you optimize for documents with 1000+ collaborators?"
        ],
        "relevant_companies": ["monday", "wix", "google"],
        "tags": ["real-time", "distributed-systems", "collaboration"]
    },
    {
        "title": "Design a Content Recommendation System",
        "difficulty": "hard",
        "problem": (
            "Design a content recommendation system that serves personalized "
            "recommendations to users based on their behavior and preferences.\n\n"
            "Requirements:\n"
            "- Serve recommendations in <100ms\n"
            "- Handle 100K requests per second\n"
            "- Support both collaborative filtering and content-based filtering\n"
            "- Update recommendations based on real-time user behavior\n"
            "- A/B testing for recommendation algorithms"
        ),
        "hints": [
            "Pre-compute recommendations offline, serve from cache",
            "Real-time signals update a lightweight model, batch retraining periodic",
            "Feature store for user/item features"
        ],
        "solution_approach": (
            "Offline pipeline: Spark/Flink for batch computation of user-item matrices, "
            "store in a feature store. Online serving: API gateway -> recommendation service "
            "reads from Redis/feature store, blends collaborative + content-based scores. "
            "Real-time: Kafka stream of user events updates lightweight features. "
            "A/B: traffic splitting at the API layer."
        ),
        "follow_ups": [
            "How would you handle the cold start problem for new users?",
            "How would you detect and prevent filter bubbles?",
            "How would you measure recommendation quality?"
        ],
        "relevant_companies": ["taboola", "outbrain", "fiverr", "wix"],
        "tags": ["ML", "distributed-systems", "real-time"]
    },
    {
        "title": "Design a Mobile Attribution System",
        "difficulty": "medium",
        "problem": (
            "Design a system that tracks which marketing campaigns led to mobile "
            "app installations and in-app events.\n\n"
            "Requirements:\n"
            "- Handle 10B+ events per day\n"
            "- Match ad clicks to app installs (attribution)\n"
            "- Support multiple attribution models (last-click, multi-touch)\n"
            "- Real-time reporting dashboard\n"
            "- Fraud detection for fake installs"
        ),
        "hints": [
            "Think about event ingestion at scale (Kafka)",
            "Attribution matching is essentially a join between click events and install events",
            "Time-series data storage for reporting"
        ],
        "solution_approach": (
            "Ingestion: API endpoints -> Kafka topics for clicks and installs. "
            "Attribution: Stream processor (Flink) matches installs to clicks within "
            "attribution window using device fingerprinting. Storage: ClickHouse or Druid "
            "for real-time analytics, S3 for raw event archive. Fraud: ML model scoring "
            "each install for anomaly patterns."
        ),
        "follow_ups": [
            "How would you handle iOS privacy changes (SKAdNetwork)?",
            "How would you deduplicate events at this scale?",
            "How would you handle clock skew between different event sources?"
        ],
        "relevant_companies": ["appsflyer", "google", "meta"],
        "tags": ["big-data", "stream-processing", "analytics"]
    },
    {
        "title": "Design a Website Builder Platform",
        "difficulty": "medium",
        "problem": (
            "Design a platform that allows non-technical users to create and host "
            "websites using a drag-and-drop editor.\n\n"
            "Requirements:\n"
            "- Drag-and-drop editor with real-time preview\n"
            "- Template library with customization\n"
            "- Custom domain support\n"
            "- Auto-scaling hosting for millions of sites\n"
            "- SEO optimization and performance"
        ),
        "hints": [
            "Separate the editor (SPA) from the rendering/hosting system",
            "Site data as JSON schema, rendered to HTML at request time or pre-built",
            "CDN for static assets, edge computing for dynamic content"
        ],
        "solution_approach": (
            "Editor: React SPA with component tree stored as JSON schema in the database. "
            "Publishing: build pipeline converts JSON to optimized HTML/CSS/JS, deploys to CDN. "
            "Hosting: Cloudflare/Fastly edge + origin servers for dynamic content. "
            "Custom domains: DNS management + automatic TLS via Let's Encrypt. "
            "Storage: PostgreSQL for site metadata, S3 for assets, Redis for editor sessions."
        ),
        "follow_ups": [
            "How would you handle millions of sites with custom domains?",
            "How would you implement undo/redo in the editor?",
            "How would you optimize for Core Web Vitals across all hosted sites?"
        ],
        "relevant_companies": ["wix", "monday", "fiverr"],
        "tags": ["web", "CDN", "editor", "hosting"]
    },
]

BEHAVIORAL_QUESTIONS: List[dict] = [
    {
        "title": "Disagreement with Technical Decision",
        "difficulty": "medium",
        "problem": (
            "Tell me about a time when you disagreed with a technical decision made "
            "by your team or manager. How did you handle it? What was the outcome?"
        ),
        "hints": [
            "Use the STAR format: Situation, Task, Action, Result",
            "Show that you can disagree respectfully and with data",
            "Emphasize the outcome, even if your suggestion was not adopted"
        ],
        "solution_approach": (
            "Good answer structure: (1) Describe the situation and the decision you disagreed with. "
            "(2) Explain WHY you disagreed (with technical reasoning, not just opinion). "
            "(3) Describe how you raised your concern (in a meeting, with data, with a POC). "
            "(4) Outcome: either your idea was adopted, or you understood why the other approach "
            "was better, or a compromise was found. (5) What you learned."
        ),
        "follow_ups": [
            "What would you do if your manager overruled you despite your data?",
            "How do you balance conviction with being a team player?"
        ],
        "relevant_companies": ["all"],
        "tags": ["behavioral", "conflict", "communication"]
    },
    {
        "title": "Project Under Pressure",
        "difficulty": "medium",
        "problem": (
            "Describe a project where you had to deliver under a very tight deadline "
            "or with significant pressure. How did you manage it?"
        ),
        "hints": [
            "Focus on how you prioritized and made trade-offs",
            "Show that you communicated proactively about risks",
            "Demonstrate both technical and interpersonal skills"
        ],
        "solution_approach": (
            "Good answer structure: (1) Context: what was the project and why the pressure? "
            "(2) Your approach: how did you break down the work, prioritize, and communicate? "
            "(3) Technical decisions: what trade-offs did you make (tech debt vs. speed)? "
            "(4) Collaboration: how did you work with the team? "
            "(5) Result: did you deliver? What was the quality? What did you learn?"
        ),
        "follow_ups": [
            "Would you do anything differently?",
            "How do you prevent tech debt accumulation from tight deadlines?"
        ],
        "relevant_companies": ["all"],
        "tags": ["behavioral", "pressure", "prioritization"]
    },
]

# Company-specific focus areas
COMPANY_FOCUS: Dict[str, Dict] = {
    "wix": {
        "name": "Wix",
        "coding_tags": ["web", "design", "cache", "string"],
        "design_tags": ["editor", "web", "CDN", "hosting"],
        "notes": "Focus on web technologies, rendering performance, and product thinking."
    },
    "monday": {
        "name": "Monday.com",
        "coding_tags": ["design", "real-time", "cache", "queue"],
        "design_tags": ["real-time", "collaboration", "distributed-systems"],
        "notes": "Focus on real-time systems, WebSocket, and collaborative features."
    },
    "checkpoint": {
        "name": "Check Point",
        "coding_tags": ["arrays", "pointers", "string", "hashing"],
        "design_tags": ["distributed-systems", "big-data"],
        "notes": "Focus on networking, security, and systems programming."
    },
    "cyberark": {
        "name": "CyberArk",
        "coding_tags": ["string", "design", "hashing"],
        "design_tags": ["distributed-systems"],
        "notes": "Focus on security, identity management, and Windows internals."
    },
    "mobileye": {
        "name": "Mobileye",
        "coding_tags": ["arrays", "math", "sorting"],
        "design_tags": ["real-time", "stream-processing"],
        "notes": "Focus on algorithms, optimization, C++, and real-time constraints."
    },
    "fiverr": {
        "name": "Fiverr",
        "coding_tags": ["design", "hash-map", "sorting"],
        "design_tags": ["web", "distributed-systems"],
        "notes": "Focus on marketplace dynamics, search/ranking, and practical system design."
    },
    "appsflyer": {
        "name": "AppsFlyer",
        "coding_tags": ["hash-map", "design", "hashing"],
        "design_tags": ["big-data", "stream-processing", "analytics"],
        "notes": "Focus on high-throughput data processing, Kafka, and real-time analytics."
    },
    "taboola": {
        "name": "Taboola",
        "coding_tags": ["sorting", "hash-map", "arrays"],
        "design_tags": ["ML", "real-time", "distributed-systems"],
        "notes": "Focus on algorithms, recommendation systems, and large-scale ML."
    },
    "outbrain": {
        "name": "Outbrain",
        "coding_tags": ["sorting", "hash-map", "arrays"],
        "design_tags": ["ML", "real-time", "distributed-systems"],
        "notes": "Focus on content recommendation, real-time bidding, and data processing."
    },
    "gong": {
        "name": "Gong",
        "coding_tags": ["string", "design", "hash-map"],
        "design_tags": ["ML", "analytics"],
        "notes": "Focus on NLP, ML pipelines, and structured FAANG-style interviews."
    },
    "snyk": {
        "name": "Snyk",
        "coding_tags": ["string", "design", "parsing"],
        "design_tags": ["distributed-systems"],
        "notes": "Focus on developer tools, security scanning, and code analysis."
    },
    "google": {
        "name": "Google Israel",
        "coding_tags": ["arrays", "hash-map", "design", "sorting", "recursion"],
        "design_tags": ["distributed-systems", "big-data", "real-time"],
        "notes": "Standard Google process. LeetCode medium-hard. System design at massive scale."
    },
    "meta": {
        "name": "Meta Israel",
        "coding_tags": ["arrays", "hash-map", "design", "linked-list"],
        "design_tags": ["distributed-systems", "real-time"],
        "notes": "Fast-paced coding (2 problems in 45 min). System design for social products."
    },
    "amazon": {
        "name": "Amazon Israel",
        "coding_tags": ["arrays", "design", "hash-map", "sorting"],
        "design_tags": ["distributed-systems", "big-data"],
        "notes": "Leadership Principles heavy. LeetCode medium. Distributed systems design."
    },
    "microsoft": {
        "name": "Microsoft Israel",
        "coding_tags": ["arrays", "design", "string", "sorting"],
        "design_tags": ["distributed-systems", "web"],
        "notes": "Generally more relaxed than other FAANG. Practical coding and design."
    },
}


def filter_questions(
    questions: List[dict],
    difficulty: Optional[str] = None,
    company: Optional[str] = None,
    topic: Optional[str] = None,
) -> List[dict]:
    """Filter questions by criteria."""
    filtered = questions

    if company and company in COMPANY_FOCUS:
        focus = COMPANY_FOCUS[company]
        tags = set(focus.get("coding_tags", []) + focus.get("design_tags", []))
        filtered = [
            q for q in filtered
            if any(t in tags for t in q.get("tags", []))
            or "all" in q.get("relevant_companies", [])
            or company in q.get("relevant_companies", [])
        ]

    if topic:
        filtered = [
            q for q in filtered
            if topic in q.get("tags", [])
            or topic.replace("-", " ") in q.get("title", "").lower()
        ]

    return filtered


def format_question(q: dict, index: int) -> str:
    """Format a question for display."""
    lines = []
    lines.append(f"\n{'=' * 60}")
    lines.append(f"  Question {index}: {q['title']}")
    difficulty = q.get("difficulty", "unknown")
    lines.append(f"  Difficulty: {difficulty.upper()}")
    lines.append(f"  Tags: {', '.join(q.get('tags', []))}")
    lines.append(f"{'=' * 60}")

    lines.append(f"\n  PROBLEM:")
    for line in q["problem"].split("\n"):
        lines.append(f"    {line}")

    lines.append(f"\n  HINTS (progressive):")
    for i, hint in enumerate(q.get("hints", []), 1):
        lines.append(f"    {i}. {hint}")

    lines.append(f"\n  SOLUTION APPROACH:")
    lines.append(f"    {q['solution_approach']}")

    if "complexity" in q:
        lines.append(f"\n  COMPLEXITY: {q['complexity']}")

    lines.append(f"\n  FOLLOW-UP QUESTIONS:")
    for fu in q.get("follow_ups", []):
        lines.append(f"    - {fu}")

    if "common_mistakes" in q:
        lines.append(f"\n  COMMON MISTAKES:")
        for cm in q.get("common_mistakes", []):
            lines.append(f"    - {cm}")

    if q.get("relevant_companies") and "all" not in q["relevant_companies"]:
        companies = [COMPANY_FOCUS.get(c, {}).get("name", c) for c in q["relevant_companies"]]
        lines.append(f"\n  RELEVANT COMPANIES: {', '.join(companies)}")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Israeli Tech Interview Question Generator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --company wix --role backend --difficulty medium
  %(prog)s --role fullstack --difficulty hard --topic system-design
  %(prog)s --difficulty easy --count 3
  %(prog)s --list-companies
  %(prog)s --list-topics
        """,
    )

    parser.add_argument("--company", type=str, help="Target company (e.g., wix, monday, checkpoint)")
    parser.add_argument("--role", type=str, help="Target role (e.g., backend, frontend, fullstack)")
    parser.add_argument("--difficulty", type=str, choices=["easy", "medium", "hard"],
                        help="Question difficulty level")
    parser.add_argument("--topic", type=str,
                        help="Specific topic (e.g., system-design, arrays, distributed-systems)")
    parser.add_argument("--count", type=int, default=3, help="Number of questions to generate (default: 3)")
    parser.add_argument("--list-companies", action="store_true", help="List supported companies")
    parser.add_argument("--list-topics", action="store_true", help="List available topics")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    parser.add_argument("--category", type=str, choices=["coding", "system-design", "behavioral", "all"],
                        default="all", help="Question category (default: all)")

    args = parser.parse_args()

    if args.list_companies:
        print("\nSupported companies:")
        print("-" * 40)
        for key, info in sorted(COMPANY_FOCUS.items()):
            print(f"  {key:<15} {info['name']}")
            print(f"  {'':15} {info['notes']}")
            print()
        return

    if args.list_topics:
        all_tags = set()
        for difficulty_questions in CODING_QUESTIONS.values():
            for q in difficulty_questions:
                all_tags.update(q.get("tags", []))
        for q in SYSTEM_DESIGN_QUESTIONS:
            all_tags.update(q.get("tags", []))

        print("\nAvailable topics:")
        print("-" * 40)
        for tag in sorted(all_tags):
            print(f"  {tag}")
        return

    # Collect candidate questions
    candidates = []

    if args.category in ("coding", "all"):
        if args.difficulty:
            coding_qs = CODING_QUESTIONS.get(args.difficulty, [])
        else:
            coding_qs = []
            for qs in CODING_QUESTIONS.values():
                coding_qs.extend(qs)
        candidates.extend(filter_questions(coding_qs, args.difficulty, args.company, args.topic))

    if args.category in ("system-design", "all"):
        sd_qs = SYSTEM_DESIGN_QUESTIONS
        if args.difficulty:
            sd_qs = [q for q in sd_qs if q.get("difficulty") == args.difficulty]
        candidates.extend(filter_questions(sd_qs, args.difficulty, args.company, args.topic))

    if args.category in ("behavioral", "all"):
        bq_qs = BEHAVIORAL_QUESTIONS
        if args.difficulty:
            bq_qs = [q for q in bq_qs if q.get("difficulty") == args.difficulty]
        candidates.extend(filter_questions(bq_qs, args.difficulty, args.company, args.topic))

    if not candidates:
        print("No questions found matching the criteria. Try broadening your search.")
        print("Use --list-companies and --list-topics to see available options.")
        sys.exit(1)

    # Select questions
    selected = random.sample(candidates, min(args.count, len(candidates)))

    # Output
    if args.json:
        output = []
        for q in selected:
            output.append({
                "title": q["title"],
                "difficulty": q.get("difficulty", "unknown"),
                "category": q.get("category", "coding"),
                "tags": q.get("tags", []),
                "problem": q["problem"],
                "hints": q.get("hints", []),
                "solution_approach": q["solution_approach"],
            })
        print(json.dumps(output, indent=2))
    else:
        header = "\nINTERVIEW PRACTICE QUESTIONS"
        if args.company and args.company in COMPANY_FOCUS:
            header += f" - {COMPANY_FOCUS[args.company]['name']}"
        if args.difficulty:
            header += f" [{args.difficulty.upper()}]"

        print(header)
        print("=" * 60)

        if args.company and args.company in COMPANY_FOCUS:
            focus = COMPANY_FOCUS[args.company]
            print(f"\n  Company notes: {focus['notes']}")

        for i, q in enumerate(selected, 1):
            print(format_question(q, i))

        print(f"\n{'=' * 60}")
        print(f"  Generated {len(selected)} question(s)")
        print(f"  Run again for different questions (randomized selection)")
        print(f"{'=' * 60}\n")


if __name__ == "__main__":
    main()
