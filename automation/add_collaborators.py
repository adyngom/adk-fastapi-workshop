#!/usr/bin/env python3
"""
GitHub Collaborator Management for Workshop Access
Automates adding/removing workshop attendees as repo collaborators
"""
import os
import sys
import csv
import time
import requests
from datetime import datetime
from typing import List, Dict
import json


class CollaboratorManager:
    """Manages GitHub repository collaborators for workshop access"""

    def __init__(self, repo_owner: str, repo_name: str, github_token: str):
        """
        Initialize the collaborator manager

        Args:
            repo_owner: GitHub username or organization (e.g., 'adyngom')
            repo_name: Repository name (e.g., 'adk-fastapi-workshop')
            github_token: GitHub personal access token with repo permissions
        """
        self.repo_owner = repo_owner
        self.repo_name = repo_name
        self.token = github_token
        self.headers = {
            "Authorization": f"token {github_token}",
            "Accept": "application/vnd.github.v3+json"
        }
        self.base_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}"

    def add_collaborator(self, username: str, permission: str = "pull") -> Dict:
        """
        Add a GitHub user as collaborator

        Args:
            username: GitHub username
            permission: 'pull' (read-only), 'push', 'admin'

        Returns:
            dict with success status and message
        """
        url = f"{self.base_url}/collaborators/{username}"

        try:
            response = requests.put(
                url,
                headers=self.headers,
                json={"permission": permission}
            )

            if response.status_code == 201:
                return {
                    "success": True,
                    "username": username,
                    "message": "Collaborator added successfully",
                    "status": "new_invitation"
                }
            elif response.status_code == 204:
                return {
                    "success": True,
                    "username": username,
                    "message": "Collaborator already exists",
                    "status": "already_added"
                }
            else:
                return {
                    "success": False,
                    "username": username,
                    "message": f"Failed: {response.status_code} - {response.text}",
                    "status": "error"
                }

        except Exception as e:
            return {
                "success": False,
                "username": username,
                "message": f"Exception: {str(e)}",
                "status": "exception"
            }

    def remove_collaborator(self, username: str) -> Dict:
        """
        Remove a GitHub user as collaborator

        Args:
            username: GitHub username

        Returns:
            dict with success status and message
        """
        url = f"{self.base_url}/collaborators/{username}"

        try:
            response = requests.delete(url, headers=self.headers)

            if response.status_code == 204:
                return {
                    "success": True,
                    "username": username,
                    "message": "Collaborator removed successfully"
                }
            else:
                return {
                    "success": False,
                    "username": username,
                    "message": f"Failed: {response.status_code}"
                }

        except Exception as e:
            return {
                "success": False,
                "username": username,
                "message": f"Exception: {str(e)}"
            }

    def bulk_add_from_csv(self, csv_file: str, permission: str = "pull") -> Dict:
        """
        Add multiple collaborators from CSV file

        CSV format:
        name,email,github_username,registered_at
        John Doe,john@example.com,johndoe,2025-10-15

        Args:
            csv_file: Path to CSV file
            permission: Access level (default: pull/read-only)

        Returns:
            dict with summary statistics
        """
        results = {
            "added": [],
            "already_exists": [],
            "failed": [],
            "total": 0
        }

        try:
            with open(csv_file, 'r') as f:
                reader = csv.DictReader(f)

                for row in reader:
                    results["total"] += 1
                    username = row.get('github_username', '').strip()

                    if not username:
                        results["failed"].append({
                            "name": row.get('name'),
                            "reason": "No GitHub username provided"
                        })
                        continue

                    print(f"Adding {username}...")
                    result = self.add_collaborator(username, permission)

                    if result["success"]:
                        if result["status"] == "new_invitation":
                            results["added"].append({
                                "username": username,
                                "name": row.get('name'),
                                "email": row.get('email')
                            })
                        else:
                            results["already_exists"].append(username)
                    else:
                        results["failed"].append({
                            "username": username,
                            "reason": result["message"]
                        })

                    # Rate limiting: GitHub allows 5000 requests/hour
                    # Be nice and wait 1 second between requests
                    time.sleep(1)

            return results

        except Exception as e:
            print(f"Error reading CSV: {str(e)}")
            sys.exit(1)

    def bulk_remove_from_csv(self, csv_file: str) -> Dict:
        """
        Remove multiple collaborators from CSV file (post-workshop cleanup)

        Args:
            csv_file: Path to CSV file with github_username column

        Returns:
            dict with summary statistics
        """
        results = {
            "removed": [],
            "failed": [],
            "total": 0
        }

        try:
            with open(csv_file, 'r') as f:
                reader = csv.DictReader(f)

                for row in reader:
                    results["total"] += 1
                    username = row.get('github_username', '').strip()

                    if not username:
                        continue

                    print(f"Removing {username}...")
                    result = self.remove_collaborator(username)

                    if result["success"]:
                        results["removed"].append(username)
                    else:
                        results["failed"].append({
                            "username": username,
                            "reason": result["message"]
                        })

                    time.sleep(1)

            return results

        except Exception as e:
            print(f"Error reading CSV: {str(e)}")
            sys.exit(1)

    def list_collaborators(self) -> List[str]:
        """Get list of current collaborators"""
        url = f"{self.base_url}/collaborators"

        try:
            response = requests.get(url, headers=self.headers)
            if response.status_code == 200:
                collaborators = response.json()
                return [c['login'] for c in collaborators]
            else:
                print(f"Failed to fetch collaborators: {response.status_code}")
                return []

        except Exception as e:
            print(f"Exception: {str(e)}")
            return []


def main():
    """Main execution"""
    import argparse

    parser = argparse.ArgumentParser(
        description="Manage GitHub collaborators for workshop access"
    )
    parser.add_argument("action", choices=["add", "remove", "list"],
                       help="Action to perform")
    parser.add_argument("--csv", help="CSV file with registrations")
    parser.add_argument("--repo", default="adyngom/adk-fastapi-workshop",
                       help="Repository in format owner/repo")
    parser.add_argument("--token", help="GitHub token (or set GITHUB_TOKEN env var)")
    parser.add_argument("--permission", default="pull",
                       choices=["pull", "push", "admin"],
                       help="Access level (default: pull)")

    args = parser.parse_args()

    # Get token
    token = args.token or os.environ.get("GITHUB_TOKEN")
    if not token:
        print("❌ Error: GitHub token required")
        print("   Set GITHUB_TOKEN environment variable or use --token")
        sys.exit(1)

    # Parse repo
    owner, name = args.repo.split("/")

    # Initialize manager
    manager = CollaboratorManager(owner, name, token)

    # Execute action
    if args.action == "list":
        print(f"📋 Current collaborators for {args.repo}:")
        collaborators = manager.list_collaborators()
        for username in collaborators:
            print(f"   - {username}")
        print(f"\n✅ Total: {len(collaborators)}")

    elif args.action == "add":
        if not args.csv:
            print("❌ Error: --csv required for add action")
            sys.exit(1)

        print(f"➕ Adding collaborators from {args.csv}...")
        results = manager.bulk_add_from_csv(args.csv, args.permission)

        print("\n" + "="*50)
        print("📊 SUMMARY")
        print("="*50)
        print(f"Total processed: {results['total']}")
        print(f"✅ Added: {len(results['added'])}")
        print(f"ℹ️  Already exists: {len(results['already_exists'])}")
        print(f"❌ Failed: {len(results['failed'])}")

        if results['failed']:
            print("\n⚠️  Failed users:")
            for failed in results['failed']:
                print(f"   - {failed}")

        # Save results for email automation
        with open('add_results.json', 'w') as f:
            json.dump(results, f, indent=2)
        print(f"\n💾 Results saved to add_results.json")

    elif args.action == "remove":
        if not args.csv:
            print("❌ Error: --csv required for remove action")
            sys.exit(1)

        confirm = input(f"⚠️  Remove collaborators from {args.csv}? (yes/no): ")
        if confirm.lower() != 'yes':
            print("❌ Cancelled")
            sys.exit(0)

        print(f"➖ Removing collaborators from {args.csv}...")
        results = manager.bulk_remove_from_csv(args.csv)

        print("\n" + "="*50)
        print("📊 SUMMARY")
        print("="*50)
        print(f"Total processed: {results['total']}")
        print(f"✅ Removed: {len(results['removed'])}")
        print(f"❌ Failed: {len(results['failed'])}")

        with open('remove_results.json', 'w') as f:
            json.dump(results, f, indent=2)
        print(f"\n💾 Results saved to remove_results.json")


if __name__ == "__main__":
    main()
