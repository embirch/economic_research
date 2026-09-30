"""Director wrapper; new work requires a branch, assignment file and explicit cap.
Historical sessions support read-only --attach --resume SESSION_ID only.
"""
import argparse
from run_agent import launch, stream_until_idle


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--title", default="Gender and AI assignment")
    parser.add_argument("--budget-usd")
    parser.add_argument("--message-file")
    parser.add_argument("--branch")
    parser.add_argument("--resume")
    parser.add_argument("--attach", action="store_true")
    args = parser.parse_args()
    if args.resume or args.attach:
        if not (args.resume and args.attach) or any([args.message_file, args.budget_usd, args.branch]):
            parser.error("Historical sessions are read-only: use --attach --resume SESSION_ID without work/budget arguments")
        import anthropic
        stream_until_idle(anthropic.Anthropic(), args.resume)
        return
    if not all([args.budget_usd, args.message_file, args.branch]):
        parser.error("New sessions require --budget-usd, --message-file and --branch")
    launch(args.budget_usd, args.message_file, "./team/agents/director.md", args.title, args.branch)


if __name__ == "__main__":
    main()
